-- PULSE.md Supabase schema
-- Run this in the Supabase SQL editor. Keep SUPABASE_SERVICE_ROLE_KEY server-side only.

create extension if not exists pgcrypto;

create table if not exists profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text unique not null,
  full_name text,
  role text not null default 'student' check (role in ('student', 'admin')),
  avatar_url text,
  last_opened_subject_id uuid,
  study_streak int not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists subjects (
  id uuid primary key default gen_random_uuid(),
  name text not null unique,
  slug text not null unique,
  description text,
  icon text default '📚',
  sort_order int not null default 0,
  is_published boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists chapters (
  id uuid primary key default gen_random_uuid(),
  subject_id uuid not null references subjects(id) on delete cascade,
  title text not null,
  slug text not null,
  description text,
  sort_order int not null default 0,
  is_published boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique(subject_id, slug)
);

create table if not exists topics (
  id uuid primary key default gen_random_uuid(),
  chapter_id uuid not null references chapters(id) on delete cascade,
  title text not null,
  slug text not null,
  overview text,
  full_notes text,
  short_notes text,
  high_yield_points jsonb not null default '[]'::jsonb,
  mnemonics jsonb not null default '[]'::jsonb,
  osce_viva jsonb not null default '[]'::jsonb,
  sort_order int not null default 0,
  is_published boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique(chapter_id, slug)
);

create table if not exists notes (
  id uuid primary key default gen_random_uuid(),
  topic_id uuid not null references topics(id) on delete cascade,
  title text not null,
  note_type text not null default 'full' check (note_type in ('full', 'short', 'high_yield', 'diagram', 'osce', 'viva')),
  content text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists resources (
  id uuid primary key default gen_random_uuid(),
  topic_id uuid references topics(id) on delete cascade,
  title text not null,
  resource_type text not null default 'link' check (resource_type in ('link', 'youtube', 'pdf', 'image', 'diagram', 'video')),
  url text not null,
  description text,
  created_at timestamptz not null default now()
);

create table if not exists quizzes (
  id uuid primary key default gen_random_uuid(),
  topic_id uuid references topics(id) on delete cascade,
  title text not null,
  description text,
  difficulty text default 'medical_student',
  created_at timestamptz not null default now()
);

create table if not exists quiz_questions (
  id uuid primary key default gen_random_uuid(),
  quiz_id uuid not null references quizzes(id) on delete cascade,
  question text not null,
  options jsonb not null default '[]'::jsonb,
  correct_answer text not null,
  explanation text,
  high_yield_tip text,
  sort_order int not null default 0,
  created_at timestamptz not null default now()
);

create table if not exists flashcards (
  id uuid primary key default gen_random_uuid(),
  topic_id uuid not null references topics(id) on delete cascade,
  front text not null,
  back text not null,
  mnemonic text,
  sort_order int not null default 0,
  created_at timestamptz not null default now()
);

create table if not exists bookmarks (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  topic_id uuid references topics(id) on delete cascade,
  resource_id uuid references resources(id) on delete cascade,
  created_at timestamptz not null default now(),
  unique(user_id, topic_id, resource_id)
);

create table if not exists user_progress (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  topic_id uuid not null references topics(id) on delete cascade,
  status text not null default 'not_started' check (status in ('not_started', 'in_progress', 'completed')),
  completion_percent int not null default 0,
  last_opened_at timestamptz not null default now(),
  completed_at timestamptz,
  created_at timestamptz not null default now(),
  unique(user_id, topic_id)
);

create table if not exists quiz_attempts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  quiz_id uuid references quizzes(id) on delete set null,
  topic_id uuid references topics(id) on delete set null,
  score int not null,
  total_questions int not null,
  answers jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create table if not exists flashcard_progress (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  flashcard_id uuid not null references flashcards(id) on delete cascade,
  rating text not null default 'good',
  reviewed_at timestamptz not null default now(),
  unique(user_id, flashcard_id)
);

alter table profiles enable row level security;
alter table subjects enable row level security;
alter table chapters enable row level security;
alter table topics enable row level security;
alter table notes enable row level security;
alter table resources enable row level security;
alter table quizzes enable row level security;
alter table quiz_questions enable row level security;
alter table flashcards enable row level security;
alter table bookmarks enable row level security;
alter table user_progress enable row level security;
alter table quiz_attempts enable row level security;
alter table flashcard_progress enable row level security;

create policy "published subjects readable" on subjects for select using (is_published = true);
create policy "published chapters readable" on chapters for select using (is_published = true);
create policy "published topics readable" on topics for select using (is_published = true);
create policy "notes readable" on notes for select using (true);
create policy "resources readable" on resources for select using (true);
create policy "quizzes readable" on quizzes for select using (true);
create policy "quiz questions readable" on quiz_questions for select using (true);
create policy "flashcards readable" on flashcards for select using (true);

create policy "own profile readable" on profiles for select using (auth.uid() = id);
create policy "own profile writable" on profiles for all using (auth.uid() = id) with check (auth.uid() = id);
create policy "own bookmarks" on bookmarks for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "own progress" on user_progress for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "own attempts" on quiz_attempts for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "own card progress" on flashcard_progress for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
