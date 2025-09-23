# GEMINI.md

## Project Overview

This project is a web-based multimedia editor. It allows users to edit video and audio files, record their screen, merge multiple media files, and convert between different media formats. The application is built as a single HTML file that includes all the necessary CSS and JavaScript. It leverages the power of `ffmpeg.wasm` to perform all the media processing tasks directly in the browser, which means no files are sent to a server.

The editor provides a user-friendly interface with the following features:

*   **Media Editing:** Trim, cut, and apply filters to video and audio files.
*   **Screen Recording:** Record the entire screen, a specific window, or a browser tab.
*   **File Merging:** Combine multiple video or audio files into a single file.
*   **Format Conversion:** Convert media files between various formats, codecs, and resolutions.
*   **Advanced Tools:** Includes a metadata editor, batch processor, and a FFmpeg command builder.

## Building and Running

This is a single-file web application, so there is no build process. To run the project, you just need to open the `media_editor.html` file in a modern web browser that supports WebAssembly.

**Steps to run the application:**

1.  Clone the repository or download the `media_editor.html` file.
2.  Open the `media_editor.html` file in a web browser like Chrome, Firefox, or Edge.

## Development Conventions

The code is written in plain JavaScript, HTML, and CSS. The JavaScript code is well-structured, with functions for different functionalities like initializing `ffmpeg.wasm`, handling file uploads, processing media, and managing the UI. The code is commented in Korean.

**Key Libraries and APIs:**

*   **FFmpeg.wasm:** A WebAssembly port of the FFmpeg command-line tool. It is used for all the media processing tasks.
*   **Web Workers:** Used to run FFmpeg in a separate thread to avoid blocking the main UI thread.
*   **IndexedDB:** Used to cache media files and settings.
*   **MediaRecorder API:** Used for screen recording.

**Code Structure:**

The JavaScript code is organized into the following sections:

*   **Global Variables:** Defines the global variables for the application.
*   **FFmpeg Initialization:** Initializes the `ffmpeg.wasm` library.
*   **IndexedDB Initialization:** Initializes the IndexedDB database.
*   **UI Functions:** Functions for managing the UI, such as switching tabs, displaying files, and showing notifications.
*   **Media Processing Functions:** Functions for processing media files, such as trimming, merging, and converting.
*   **Screen Recording Functions:** Functions for starting, stopping, and pausing screen recording.
*   **Utility Functions:** Helper functions for formatting file sizes, time, etc.
*   **Event Listeners:** Event listeners for handling user interactions.
