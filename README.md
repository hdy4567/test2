# GitHub 토론 분서 분석 도구

최근 GitHub에서 가장 핫한 토론을 4가지 관점으로 분석하는 Python 도구입니다.

## 특징

### 4가지 분석 관점

1. **#문제정의**
   - 해결하려는 핵심 문제
   - 솔루션 접근법
   - 사용 사례

2. **#아키텍처_툴**
   - 시스템 아키텍처 다이어그램
   - 기술 스택 상세
   - 핵심 구성요소

3. **#데이터플로우**
   - 개발 단계부터 런타임까지 전체 흐름
   - 비동기 처리 방식
   - 데이터 구조

4. **#문서화**
   - 문서 구조와 철학
   - 접근법 및 특징
   - 커뮤니티 지원

## 설치 및 사용법

### 요구사항

- Python 3.7+

### 실행

```bash
python github_discussion_analyzer.py
```

## 출력 파일

1. **github_discussion_analysis.md**: Markdown 형식의 분석 리포트
2. **analysis_data.json**: JSON 형식의 분석 데이터

## 현재 분석 대상

- **Valdi**: Snapchat의 크로스플랫폼 UI 프레임워크
- **React 19**: Concurrent Rendering 및 새로운 기능
- **n8n**: 워크플로우 자동화 플랫포

## 라이센스

MIT License

## 기여

이슈나 PR을 통해 자유롭게 기여해주세요!

---

**기반**: Slack #일반 채널의 GitHub 토론 분석 리포트 (2025-11-26)
