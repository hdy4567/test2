#!/usr/bin/env python3
"""
GitHub 토론 분석 도구
최근 GitHub에서 가장 핫한 토론을 4가지 관점으로 분석합니다.
- #문제정의: 해결하려는 핵심 문제, 솔루션 접근법, 사용 사례
- #아키텍처_툴: 시스템 아키텍처 다이어그램, 기술 스택 상세, 핵심 구성요소
- #데이터플로우: 개발 단계부터 런타임까지 전체 흐름, 비동기 처리 방식, 데이터 구조
- #문서화: 문서 구조와 철학, 접근법 및 특징, 커뮤니티 지원
"""

import json
import sys
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class DiscussionAnalysis:
    """토론 분석 데이터 클래스"""
    project_name: str
    stars: int
    category: str
    
    # #문제정의
    core_problem: str
    solution_approach: str
    use_cases: List[str]
    
    # #아키텍처_툴
    architecture_diagram: str
    tech_stack: Dict[str, str]
    core_components: List[str]
    
    # #데이터플로우
    data_flow: str
    async_processing: str
    data_structure: str
    
    # #문서화
    documentation_structure: List[str]
    documentation_philosophy: str
    community_support: str


class GitHubDiscussionAnalyzer:
    """
    GitHub 토론 분석기
    """
    
    def __init__(self):
        self.analyses: List[DiscussionAnalysis] = []
        self.report_date = datetime.now().strftime("%Y년 %m월 %d일")
    
    def add_analysis(self, analysis: DiscussionAnalysis):
        """분석 결과 추가"""
        self.analyses.append(analysis)
    
    def generate_markdown_report(self) -> str:
        """
        Markdown 형식의 분석 리포트 생성
        """
        report = f"# GitHub 토론 분석 리포트\n\n"
        report += f"> 생성일: {self.report_date}\n"
        report += f"> 분석 대상: {', '.join([a.project_name for a in self.analyses])}\n\n"
        report += "---\n\n"
        
        for i, analysis in enumerate(self.analyses, 1):
            report += f"## {i}. {analysis.project_name}\n\n"
            report += f"**카테고리**: {analysis.category}\n"
            report += f"**Stars**: {analysis.stars:,}\n\n"
            
            # 문제정의
            report += "### #문제정의\n\n"
            report += f"**핵심 문제**\n{analysis.core_problem}\n\n"
            report += f"**솔루션 접근법**\n{analysis.solution_approach}\n\n"
            report += "**사용 사례**\n"
            for use_case in analysis.use_cases:
                report += f"- {use_case}\n"
            report += "\n"
            
            # 아키텍처_툴
            report += "### #아키텍처_툴\n\n"
            report += "**시스템 아키텍처**\n"
            report += f"```\n{analysis.architecture_diagram}\n```\n\n"
            report += "**기술 스택**\n"
            for key, value in analysis.tech_stack.items():
                report += f"- **{key}**: {value}\n"
            report += "\n**핵심 구성요소**\n"
            for component in analysis.core_components:
                report += f"- {component}\n"
            report += "\n"
            
            # 데이터플로우
            report += "### #데이터플로우\n\n"
            report += f"**전체 흐름**\n```\n{analysis.data_flow}\n```\n\n"
            report += f"**비동기 처리**\n{analysis.async_processing}\n\n"
            report += f"**데이터 구조**\n{analysis.data_structure}\n\n"
            
            # 문서화
            report += "### #문서화\n\n"
            report += "**문서 구조**\n"
            for doc in analysis.documentation_structure:
                report += f"- {doc}\n"
            report += f"\n**문서화 철학**\n{analysis.documentation_philosophy}\n\n"
            report += f"**커뮤니티 지원**\n{analysis.community_support}\n\n"
            
            report += "---\n\n"
        
        return report
    
    def save_report(self, filename: str = "analysis_report.md"):
        """분석 리포트를 파일로 저장"""
        report = self.generate_markdown_report()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✅ 분석 리포트가 {filename}에 저장되었습니다.")
    
    def export_json(self, filename: str = "analysis_data.json"):
        """분석 데이터를 JSON 형식으로 내보내기"""
        data = {
            "report_date": self.report_date,
            "analyses": [asdict(a) for a in self.analyses]
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 분석 데이터가 {filename}에 저장되었습니다.")


def create_sample_analyses() -> List[DiscussionAnalysis]:
    """
    샘플 분석 데이터 생성 (Slack #일반 채널의 최근 메시지 기반)
    """
    
    # 1. Valdi 분석
    valdi = DiscussionAnalysis(
        project_name="Valdi",
        stars=13434,
        category="크로스플랫폼 UI 프레임워크",
        
        core_problem="크로스 플랫포 개발에서 속도와 런타임 성능 사이의 트레이드오프. "
                       "웹뷰 기반 프레임워크들은 네이티브 성능을 확보하지 못하고, JavaScript 브리지 의존으로 "
                       "통신 오버헤드가 발생하며, 느린 컴파일 사이클로 개발 속도가 저하됩니다.",
        
        solution_approach="TypeScript로 작성된 선언형 UI를 네이티브 뷰로 직접 컴파일하여 웹뷰나 JS 브리지 없이 "
                          "진정한 네이티브 성능을 제공합니다. Snap의 프로덕션 앱에서 8년간 검증된 솔루션입니다.",
        
        use_cases=[
            "크로스플랫폼 모바일 앱 개발 (iOS, Android, macOS)",
            "고성능이 요구되는 네이티브 앱 개발",
            "빠른 프로토타입 및 Hot Reload를 통한 반복 개발"
        ],
        
        architecture_diagram="User Interaction\n    ↓\nTypeScript Event Handlers\n    ↓\nComponent State Update\n    ↓\nC++ Layout Engine\n    ↓\nNative View Update (Recycled)\n    ↓\nPlatform Rendering",
        
        tech_stack={
            "UI 선언": "TypeScript/TSX",
            "Layout Engine": "C++ (메인 스레드 최적화)",
            "Native Bindings": "Swift, Kotlin, Objective-C",
            "Build System": "Valdi CLI + Bazel",
            "개발 도구": "VSCode/Cursor extensions, Hermes Debugger"
        },
        
        core_components=[
            "Automatic view recycling: 글로벌 뷰 풀링으로 인플레이션 지연시간 감소",
            "Component-level rendering: 부모 재렌더링 없이 독립적 업데이트",
            "Viewport-aware rendering: 보이는 뷰만 인플레이트",
            "Optimized C++ layout: 메인 스레드에서 최소 마샔링 오버헤드"
        ],
        
        data_flow="[1] Development: TSX → Valdi Compiler → Native Code + Bindings → Hot Reload\n"
                  "[2] Runtime: User Action → TS Handlers → State Update → C++ Layout → Native View Update → Platform Render\n"
                  "[3] Native Integration: TS ↔ Native API ↔ Type-safe Modules ↔ Protobuf Serialization",
        
        async_processing="Worker Thread Architecture를 통한 Background JS 실행. "
                        "Main Thread ↔ Worker Threads 간 Message Passing 및 Native API 접근 지원.",
        
        data_structure="Type-safe polyglot modules를 통한 양방향 콜백. Protobuf 직렬화로 효율적인 데이터 전송.",
        
        documentation_structure=[
            "Getting Started: Quick start, Installation, VSCode Setup, Codelabs",
            "Core Concepts: Component lifecycle, Flexbox layout with RTL, Touch handling, State management",
            "Advanced: Native bindings, Worker threads, Animations, Protobuf, Full-stack architecture",
            "Development Workflow: Hot reload, Hermes debugger, Testing, Bazel build",
            "Performance: View recycling, Profiling guide, Best practices"
        ],
        
        documentation_philosophy="실용적(실제 사용 사례 중심), 점진적(기본부터 고급까지), "
                                 "통합적(API 레퍼런스 + 예제), 커뮤니티 중심(Discord + FAQ)",
        
        community_support="Discord 커뮤니티 지원, FAQ, 활발한 GitHub 이슈 트래킹"
    )
    
    # 2. React 19 분석
    react19 = DiscussionAnalysis(
        project_name="React 19",
        stars=234000,
        category="JavaScript UI 라이브러리",
        
        core_problem="복잡한 UI 상호작용과 비동기 데이터 처리에서의 성능 및 사용자 경험 문제. "
                       "기존 React는 동기적 렌더링으로 인한 블로킹, 복잡한 상태 관리, 서버 컴포넌트 부재 문제가 있었습니다.",
        
        solution_approach="Concurrent Rendering을 통한 비동기 렌더링 개선, Server Components로 서버 측 렌더링 지원, "
                          "Actions API로 폼 처리 간소화, use() Hook으로 비동기 데이터 처리 개선.",
        
        use_cases=[
            "대규모 SPA(Single Page Application) 개발",
            "서버 사이드 렌더링이 필요한 성능 최적화",
            "복잡한 상태 관리가 필요한 엔터프라이즈 앱"
        ],
        
        architecture_diagram="User Action\n    ↓\nReact Component\n    ↓\nConcurrent Renderer (Fiber)\n    ↓\nVirtual DOM Reconciliation\n    ↓\nDOM Update (Batched)\n    ↓\nBrowser Rendering",
        
        tech_stack={
            "Core": "JavaScript/TypeScript",
            "Rendering": "Fiber Architecture (Concurrent Mode)",
            "Server": "React Server Components (RSC)",
            "State": "useState, useReducer, Context API",
            "Build": "Vite, Next.js, Create React App"
        },
        
        core_components=[
            "Concurrent Rendering: 우선순위 기반 비동기 렌더링",
            "Server Components: 서버 측에서 렌더링되는 컴포넌트",
            "Actions: 폼 제출 및 데이터 변경 처리 간소화",
            "use() Hook: Promise 및 Resource 직접 처리"
        ],
        
        data_flow="Component Render → Virtual DOM 생성 → Reconciliation (차이 계산) → "
                  "Commit Phase (DOM 업데이트) → Effects 실행",
        
        async_processing="Concurrent Mode로 렌더링 작업을 일시 중단하고 우선순위가 높은 작업을 먼저 처리. "
                        "Suspense를 통한 비동기 데이터 로딩 처리.",
        
        data_structure="Fiber 트리 구조로 컴포넌트 계층 표현. Virtual DOM으로 효율적인 DOM 업데이트.",
        
        documentation_structure=[
            "Getting Started: 설치, 기본 개념, 컴포넌트 작성",
            "Hooks: useState, useEffect, useContext, useMemo, useCallback, use()",
            "Advanced: Concurrent Features, Server Components, Actions",
            "Performance: Memoization, Code Splitting, Lazy Loading",
            "Best Practices: 설계 패턴, 테스팅, 디버깅"
        ],
        
        documentation_philosophy="단계별 학습 경로, 상세한 API 문서, 실제 예제 기반 설명, "
                                 "커뮤니티 피드백 반영",
        
        community_support="대규모 GitHub 커뮤니티, Stack Overflow, Discord, React Conf 컨퍼런스"
    )
    
    # 3. n8n 분석
    n8n = DiscussionAnalysis(
        project_name="n8n",
        stars=45000,
        category="워크플로우 자동화 플랫폼",
        
        core_problem="비기술자도 복잡한 비즈니스 프로세스를 자동화할 수 있도록 하면서 "
                       "개발자는 코드를 통한 확장 가능성을 유지해야 하는 문제. "
                       "SaaS 자동화 툴의 비용과 데이터 프라이버시 문제.",
        
        solution_approach="노드 기반 비주얼 워크플로우 에디터로 누구나 쉽게 사용 가능. "
                          "350+ 통합 노드 제공, 자체 호스팅 가능, JavaScript/TypeScript로 커스텀 노드 작성 지원.",
        
        use_cases=[
            "API 통합 자동화 (Slack, Google Sheets, GitHub 등)",
            "데이터 동기화 및 ETL 파이프라인",
            "비즈니스 프로세스 자동화 (CRM, 마케팅, 판매)"
        ],
        
        architecture_diagram="User (Visual Editor)\n    ↓\nWorkflow Definition (JSON)\n    ↓\nExecution Engine\n    ↓\nNode Execution (Sequential/Parallel)\n    ↓\nIntegrations (350+ Services)\n    ↓\nOutput/Webhook",
        
        tech_stack={
            "Backend": "Node.js, TypeScript, Express",
            "Frontend": "Vue.js 3, TypeScript",
            "Database": "SQLite, PostgreSQL, MySQL",
            "Queue": "Bull (Redis-based)",
            "Deployment": "Docker, Kubernetes, npm"
        },
        
        core_components=[
            "Visual Workflow Editor: 드래그 앤 드롭 인터페이스",
            "Execution Engine: 노드 기반 순차/병렬 실행",
            "Integration Nodes: 350+ 서비스 통합",
            "Custom Code: JavaScript/TypeScript 코드 노드"
        ],
        
        data_flow="Workflow Trigger (Webhook/Schedule/Manual) → Node Queue → 순차 실행 → "
                  "데이터 변환 → API 호출 → 결과 저장/전송",
        
        async_processing="Queue 기반 비동기 실행. Webhook 트리거 지원. 스케줄 기반 자동 실행. "
                        "병렬 노드 실행 지원.",
        
        data_structure="JSON 기반 워크플로우 정의. 노드 간 데이터 흐름은 Key-Value 쌍 구조.",
        
        documentation_structure=[
            "Getting Started: Installation, 첨 워크플로우 생성",
            "Nodes: 각 통합 노드별 상세 가이드",
            "Workflows: 패턴, 베스트 프랙티스, 예제",
            "Development: 커스텀 노드 개발, API 문서",
            "Deployment: Self-hosting, Cloud, Docker"
        ],
        
        documentation_philosophy="실용적 예제 중심, 상세한 노드 별 가이드, 커뮤니티 컨트리뷔션 활발",
        
        community_support="활발한 Forum, Discord, GitHub Discussions, 커뮤니티 노드 파트너 프로그램"
    )
    
    return [valdi, react19, n8n]


def main():
    """
    메인 실행 함수
    """
    print("\n✨ GitHub 토론 분석 도구 실행 중...\n")
    
    # 분석기 생성
    analyzer = GitHubDiscussionAnalyzer()
    
    # 샘플 분석 데이터 추가
    sample_analyses = create_sample_analyses()
    for analysis in sample_analyses:
        analyzer.add_analysis(analysis)
    
    # 분석 리포트 출력
    print("=" * 80)
    print(analyzer.generate_markdown_report())
    print("=" * 80)
    
    # 파일로 저장
    analyzer.save_report("github_discussion_analysis.md")
    analyzer.export_json("analysis_data.json")
    
    print("\n✅ 분석 완료!\n")


if __name__ == "__main__":
    main()
