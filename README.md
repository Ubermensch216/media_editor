# 🎬 MultiMedia Editor Pro

> **FFmpeg.wasm 기반의 강력한 100% 클라이언트 사이드 웹 멀티미디어 에디터**  
> 서버 업로드 없이 브라우저 내에서 비디오/오디오 편집, 화면 녹화, 포맷 변환 및 파일 병합을 안전하고 빠르게 처리하세요.

---

## 💡 주요 특징 (Key Features)

- **🔒 100% 개인정보 보호 (Privacy-First)**: 모든 미디어 처리가 사용자의 브라우저(WebAssembly) 내에서만 수행됩니다. 파일이 외부 서버로 전송되지 않습니다.
- **⚡ 무설치 / 빌드 프리 (Zero Setup)**: 별도의 설치나 컴파일 과정 없이 `media_editor.html` 파일 하나만 브라우저로 열면 즉시 사용 가능합니다.
- **📱 PWA & 오프라인 지원**: Service Worker와 IndexedDB를 탑재하여 오프라인 환경에서도 안정적인 작업을 지원합니다.
- **🎛️ 올인원 미디어 솔루션**: 비디오·오디오 트림/자르기, 화면 및 웹캠 녹화, 파일 합치기, 포맷 및 코덱 변환, 메타데이터 편집까지 다양한 기능을 제공합니다.

---

## 🚀 주요 기능 (Core Capabilities)

### 1. ✂️ 영상 / 음성 편집 (Media Edit & Filter)
- **타임라인 & 파형(Waveform)**: 직관적인 인터페이스로 시작/종료 지점을 지정하여 구간 추출
- **미세 조절**: 재생 속도(0.25x ~ 4.0x) 및 음량(0% ~ 200%) 설정
- **비디오 필터**: 흑백, 블러, 엣지 검출, 세피아, 네거티브, 밝기/대비 실시간 조정

### 2. 🎥 화면 및 웹캠 녹화 (Screen Recording & PIP)
- **녹화 대상 지정**: 전체 화면, 특정 애플리케이션 창, 브라우저 탭 선택 지원
- **오디오 캡처**: 시스템 소리 및 마이크 음성 동시/선택 녹음
- **화질 & 프레임율**: SD부터 8K(4320p) 해상도 및 15~60 FPS 선택
- **웹캠 PIP(Picture-in-Picture)**: 화면 녹화와 웹캠 오버레이 화면 동시 기록 (위치 지정 가능)

### 3. 🔗 파일 합치기 (File Merge & Transitions)
- **드래그 앤 드롭 정렬**: 여러 영상/음성 파일의 순서를 손쉽게 변경
- **다양한 트랜지션**: 페이드(Fade), 디졸브(Dissolve), 와이프(Wipe), 슬라이드(Slide) 효과 지원
- **출력 포맷 지정**: MP4, AVI, MKV, WEBM, MP3, WAV 등 원하는 형식으로 병합

### 4. 🔄 형식 및 코덱 변환 (Format & Codec Conversion)
- **포맷 변환**: 
  - 비디오: MP4, AVI, MKV, WEBM, MOV, FLV, WMV
  - 오디오: MP3, WAV, AAC, OGG, FLAC, M4A
  - 이미지: Animated GIF
- **세부 코덱 제어**: H.264, H.265/HEVC, VP8, VP9, AV1, AAC, Opus, FLAC 등 지원
- **고급 옵션**: 해상도 축소/확대, 비디오/오디오 비트레이트 조절, 오디오/비디오 트랙 제거

### 5. ⚙️ 고급 도구 (Advanced Tools)
- **FFmpeg 명령어 생성기**: GUI 조작을 통해 실제 실행 가능한 `ffmpeg` CLI 커맨드 자동 생성
- **메타데이터 편집기**: 미디어 파일의 아티스트, 앨범, 제목 등 태그 정보 수정
- **일괄 처리 (Batch Processor)**: 다량의 파일에 동일한 변환/편집 작업 적용
- **음성/프레임 추출**: 비디오에서 MP3 오디오만 추출하거나 주요 프레임을 이미지로 캡처
- **캐시 및 성능 관리**: IndexedDB 용량 제어, Web Worker 멀티스레딩 지원

---

## 🛠️ 기술 스택 (Tech Stack)

| 구분 | 기술 / 라이브러리 |
| :--- | :--- |
| **Frontend** | HTML5, Vanilla CSS3, JavaScript (ES6+) |
| **Media Processing** | [FFmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm) (`@ffmpeg/ffmpeg`, `@ffmpeg/core`) |
| **Recording API** | HTML5 MediaRecorder API, Screen Capture API |
| **Storage & Offline** | IndexedDB API, Service Worker API (PWA) |

---

## 💻 실행 방법 (Getting Started)

1. 이 저장소를 클론(Clone)하거나 다운로드합니다.
2. 실행하려는 브라우저(Chrome, Edge, Firefox 등 최신 웹브라우저 권장)에서 `media_editor.html` 파일을 엽니다.
3. 파일 조작 및 녹화 기능을 바로 이용하실 수 있습니다.

> 💡 **참고 (Browser Compatibility)**  
> FFmpeg.wasm의 성능 향상 및 멀티스레딩(SharedArrayBuffer) 활용을 위해 최신 Chromium 기반 브라우저(Chrome, Edge) 이용을 권장합니다.

---

## 📁 주요 파일 구조 (File Structure)

```text
.
├── media_editor.html           # 메인 멀티미디어 에디터 애플리케이션 (통합 버전)
├── screen_recorder.html        # 화면 녹화 전용 사이드바 툴 모듈
├── screen_recording.html       # 화면 녹화 전문 모듈
├── screen_recording_codec.html # 코덱 상세 설정 특화 화면 녹화 툴
├── GEMINI.md                   # 개발자 및 LLM 가이드용 프로젝트 기술 문서
└── README.md                   # 프로젝트 소개 문서
```
