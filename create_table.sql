-- Carrot 앱용 names 테이블 생성
CREATE TABLE IF NOT EXISTS names (
  id BIGSERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- RLS (Row Level Security) 활성화
ALTER TABLE names ENABLE ROW LEVEL SECURITY;

-- 모든 사용자가 읽을 수 있도록 설정
CREATE POLICY "Allow public read" ON names
  FOR SELECT USING (true);

-- 모든 사용자가 삽입할 수 있도록 설정
CREATE POLICY "Allow public insert" ON names
  FOR INSERT WITH CHECK (true);
