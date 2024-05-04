import subprocess
import customtkinter as ctk
from tkinter import filedialog
# from pytube import YouTube
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class GUI:
    def __init__(self):
        self.root = ctk.CTk()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.setup_gui()
    
    def setup_gui(self):
        self.root.title("GSM Arena Product Review Crawler")
        self.root.geometry("720x540")
        self.root.minsize(540, 540)
        self.root.maxsize(540, 540)
        self.content_frame = ctk.CTkFrame(self.root)
        self.content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)
        self.url_label = ctk.CTkLabel(self.content_frame, text="Insert your product review URL: ")
        self.entry_url = ctk.CTkEntry(self.content_frame, width=400, height=40)
        self.url_label.pack(pady=(10, 5))
        self.entry_url.pack(pady=(10, 5))
        
        self.option_frame = ctk.CTkFrame(self.content_frame, width=300, height=50, corner_radius=10)
        self.input_types = ["URL file", "URL"]
        self.input_type_cmb = ctk.CTkComboBox(self.option_frame, values=self.input_types, state='readonly', command=self.update_res_cmb)
        self.input_type_cmb.set(self.input_types[-1])
        self.input_type_cmb.pack(side=ctk.LEFT, pady=(10, 5), padx=10)
        self.choose_file_btn = ctk.CTkButton(self.option_frame, text="Choose File", command=self.choose_file)
        self.choose_file_btn.configure(state=ctk.DISABLED)
        self.choose_file_btn.pack(side=ctk.RIGHT, pady=(10, 5), padx=10)
        self.option_frame.pack(pady=(10, 5))
        
        self.button_frame = ctk.CTkFrame(self.content_frame, width=300, height=50, corner_radius=10)
        self.download_button = ctk.CTkButton(self.button_frame, text="Crawl data", command=self.crawl_data)
        self.download_button.pack(side=ctk.LEFT, pady=(10, 5), padx=10)
        self.button_frame.pack(pady=(10, 5))
        
        self.progress_frame = ctk.CTkScrollableFrame(self.content_frame, width=400, height=280, corner_radius=10, border_width=1)
        
        # self.progress_frame.add(ctk.CTkLabel(self.progress_frame, text="Progress:"))
        self.progress_label = ctk.CTkLabel(self.progress_frame, text="PROGRESS")
        self.progress_label.pack(pady=(10, 5))
        self.progress_frame.pack(pady=(10, 5))
        
        
    def run(self):
        self.root.mainloop()
        
    def choose_file(self):
        file_path = filedialog.askopenfilename(title="Select File")
        if file_path:
            self.entry_url.delete(0, ctk.END)
            self.entry_url.insert(0, file_path)
        
    def update_res_cmb(self, selected):
        if selected != 'URL file':
            self.choose_file_btn.configure(state=ctk.DISABLED)
        else:
            self.choose_file_btn.configure(state=ctk.NORMAL)

    def crawl_data(self):
        url = self.entry_url.get()
        input_type = self.input_type_cmb.get()
        urls = []
        output_file = filedialog.asksaveasfilename(title="Save File As", defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if input_type == 'URL file':
            with open(url, 'r') as file:
                urls = file.readlines()
                for url in urls:
                    print(url)
        else:
            urls.append(url)
        self.generate_files(url, output_file)
        self.run_command()
        
        # try:
        #     url = self.entry_url.get()
        #     yt = YouTube(url)
        #     self.author_label.configure(text=f"Author: {yt.author}")
        #     self.length_label.configure(text=f"Length: {yt.length // 60} minutes {yt.length % 60} seconds")
        #     self.title_label.configure(text=f"Title: {yt.title}")
        #     self.views_label.configure(text=f"Views: {yt.views:,}")
        #     self.info_frame.pack(pady=(10, 5))
        # except Exception as e:
        #     self.reset()
        #     self.status_label.configure(text=f"Error: {str(e)}")
    
    def generate_files(self, url, output_path):
        sh_file_content = f"cd ..\\gsm_arena_product_review\\gsm_arena_product_review\nscrapy crawl gsm_arena_product_review -o {output_path} -a start_url={url}\ncd ..\\..\\gui_app"
        bat_file_content = f"cd ..\\gsm_arena_product_review\\gsm_arena_product_review\nscrapy crawl gsm_arena_product_review -o {output_path} -a start_url={url}\ncd ..\\..\\gui_app"
        
        with open("generate.sh", "w") as sh_file:
            sh_file.write(sh_file_content)
        
        with open("generate.bat", "w") as bat_file:
            bat_file.write(bat_file_content)
    
    def run_command(self):
        filepath = "generate.bat"
        p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
        stdout, stderr = p.communicate()
        if stderr is not None:
            filepath = "generate.sh"
            p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
            stdout, stderr = p.communicate()
            if stderr is not None:
                return False
        return True

    def on_progress(self, stream, chunk, bytes_remaining):
        # total_size = stream.filesize
        # downloaded_bytes = total_size - bytes_remaining
        # completed_percentage = downloaded_bytes / total_size * 100
        # print(completed_percentage)
        # self.progress_label.configure(text=str(int(completed_percentage)) + '%')
        # self.progress_bar.update()
        # self.progress_bar.set(completed_percentage / 100)
        pass

    def reset(self):
        # self.progress_label.pack(pady=(10, 5))
        # self.progress_bar.pack(pady=(10, 5))
        # self.status_label.pack(pady=(10, 5))
        # self.progress_bar.update()
        # self.progress_bar.set(0.0)
        # self.progress_label.configure(text="0%")
        # self.status_label.configure(text="")
        # self.info_frame.pack_forget()
        pass 

    def download_video(self):
        # url = self.entry_url.get()
        # resolution = self.resolution_cmb.get()
        # print(f'{url}, {resolution}')
        # self.reset()
        # self.entry_url.configure(state=ctk.DISABLED)
        # self.download_button.configure(state=ctk.DISABLED)
        # self.show_info_button.configure(state=ctk.DISABLED)
        # download_dir = filedialog.askdirectory(title="Select Download Location")
        # if not download_dir:
        #     print("Download cancelled by user.")
        #     self.entry_url.configure(state=ctk.NORMAL)
        #     self.download_button.configure(state=ctk.NORMAL)
        #     return
        # try:
        #     yt = YouTube(url, on_progress_callback=self.on_progress)
        #     if self.input_type_cmb.get() == 'audio':
        #         stream = yt.streams.filter(only_audio=True).first()
        #         file_name = stream.download(output_path=download_dir)
        #         base, ext = os.path.splitext(file_name)
        #         new_file = base + '.mp3'
        #         os.rename(file_name, new_file)
        #     else:
        #         stream = yt.streams.filter(res=resolution, only_audio=False).first()
        #         stream.download(output_path=download_dir)
        #     self.status_label.configure(text="Downloaded successfully!")
        #     print("success")
        # except Exception as e:
        #     print(e)
        #     self.status_label.configure(text=f"Error: {str(e)}")
        # finally:
        #     self.entry_url.configure(state=ctk.NORMAL)
        #     self.download_button.configure(state=ctk.NORMAL)
        #     self.show_info_button.configure(state=ctk.NORMAL)
        pass

if __name__ == "__main__":
    downloader = GUI()
    downloader.run()