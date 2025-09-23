
import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Get the absolute path of the HTML file
        import os
        html_file_path = os.path.abspath("D:\Dev\media_editor\media_editor.html")

        await page.goto(f"file://{html_file_path}")

        # Wait for FFmpeg to load
        await expect(page.locator("#loadingOverlay")).to_be_hidden(timeout=60000)
        await expect(page.locator("text=FFmpeg 준비 완료!")).to_be_visible()

        print("Page loaded and FFmpeg is ready.")

        # Test tab switching
        print("Testing tab switching...")
        await page.click("text=화면 녹화")
        await expect(page.locator("#record")).to_be_visible()
        print("Record tab is visible.")
        await page.click("text=파일 합치기")
        await expect(page.locator("#merge")).to_be_visible()
        print("Merge tab is visible.")
        await page.click("text=형식 변환")
        await expect(page.locator("#convert")).to_be_visible()
        print("Convert tab is visible.")
        await page.click("text=고급 설정")
        await expect(page.locator("#advanced")).to_be_visible()
        print("Advanced tab is visible.")
        await page.click("text=영상/음성 편집")
        await expect(page.locator("#edit")).to_be_visible()
        print("Edit tab is visible.")
        print("Tab switching test passed.")

        # Test file upload
        print("Testing file upload...")
        # Create a dummy file for testing
        with open("test_video.mp4", "w") as f:
            f.write("dummy video file")
        
        await page.locator("#fileInput").set_input_files("test_video.mp4")
        await expect(page.locator(".file-item")).to_be_visible()
        print("File upload test passed.")

        # Test media trimming
        print("Testing media trimming...")
        await page.fill("#startTime", "00:00:01")
        await page.fill("#endTime", "00:00:03")
        
        async with page.expect_download() as download_info:
            await page.click("text=구간 추출")
        
        download = await download_info.value
        await download.save_as("trimmed_video.mp4")
        print("Media trimming test passed.")

        # Test format conversion
        print("Testing format conversion...")
        await page.click("text=형식 변환")
        await page.locator("#convertFileInput").set_input_files("test_video.mp4")
        await page.select_option("#convertFormat", "mp3")
        
        async with page.expect_download() as download_info:
            await page.click("text=변환 시작")
            
        download = await download_info.value
        await download.save_as("converted_audio.mp3")
        print("Format conversion test passed.")

        # Test file merging
        print("Testing file merging...")
        await page.click("text=파일 합치기")
        await page.locator("#mergeFileInput").set_input_files(["test_video.mp4", "test_video.mp4"])
        
        async with page.expect_download() as download_info:
            await page.click("text=파일 합치기 시작")
        
        download = await download_info.value
        await download.save_as("merged_video.mp4")
        print("File merging test passed.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
