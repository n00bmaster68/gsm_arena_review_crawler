import subprocess
import customtkinter as ctk
from tkinter import filedialog, messagebox
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
        self.root.geometry("540x360")
        self.root.minsize(540, 360)
        self.root.maxsize(540, 360)
        self.content_frame = ctk.CTkFrame(self.root)
        self.content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)
        self.url_label = ctk.CTkLabel(self.content_frame, text="Insert your product review URL: ")
        self.entry_url = ctk.CTkEntry(self.content_frame, width=400, height=40)
        self.url_label.pack(pady=(10, 5))
        self.entry_url.pack(pady=(10, 5))
        
        self.option_frame = ctk.CTkFrame(self.content_frame, width=300, height=50, corner_radius=10)
        self.input_types = ["URL file", "URL"]
        self.input_type_cmb = ctk.CTkComboBox(self.option_frame, values=self.input_types, state='readonly', command=self.update_type_cmb)
        self.input_type_cmb.set(self.input_types[-1])
        self.input_type_cmb.pack(side=ctk.LEFT, pady=(10, 5), padx=10)
        self.choose_file_btn = ctk.CTkButton(self.option_frame, text="Choose File", command=self.choose_file)
        self.choose_file_btn.configure(state=ctk.DISABLED)
        self.choose_file_btn.pack(side=ctk.RIGHT, pady=(10, 5), padx=10)
        self.option_frame.pack(pady=(10, 5))
        
        self.button_frame = ctk.CTkFrame(self.content_frame, width=300, height=50, corner_radius=10)
        self.crawl_button = ctk.CTkButton(self.button_frame, text="Crawl data", command=self.crawl_data)
        self.crawl_button.pack(side=ctk.LEFT, pady=(10, 5), padx=10)
        self.button_frame.pack(pady=(10, 5))
        
        # self.progress_frame = ctk.CTkScrollableFrame(self.content_frame, width=400, height=280, corner_radius=10, border_width=1)
        
        # # self.progress_frame.add(ctk.CTkLabel(self.progress_frame, text="Progress:"))
        # self.progress_label = ctk.CTkLabel(self.progress_frame, text="PROGRESS")
        # self.progress_label.pack(pady=(10, 5))
        # self.progress_frame.pack(pady=(10, 5))
        
        
    def run(self):
        self.root.mainloop()
        
    def choose_file(self):
        file_path = filedialog.askopenfilename(title="Select File")
        if file_path:
            self.entry_url.delete(0, ctk.END)
            self.entry_url.insert(0, file_path)
        
    def update_type_cmb(self, selected):
        if selected != 'URL file':
            self.choose_file_btn.configure(state=ctk.DISABLED)
            # self.entry_url.configure(state=ctk.NORMAL)
            # self.entry_url.configure(text="")
            self.entry_url.delete(0, ctk.END)
            self.url_label.configure(text="Insert your product review URL: ")
        else:
            self.choose_file_btn.configure(state=ctk.NORMAL)
            self.entry_url.delete(0, ctk.END)
            # self.entry_url.configure(state=ctk.DISABLED)
            # self.entry_url.configure(text="")
            self.url_label.configure(text="Choose your URL list file: ")

    def crawl_data(self):
        url = self.entry_url.get()
        input_type = self.input_type_cmb.get()
        self.crawl_button.configure(state=ctk.DISABLED)
        if input_type == 'URL file':
            try:
                with open(url, 'r') as file:
                    urls = file.readlines()
                    output_dir = filedialog.askdirectory(title="Select Output Directory")
                    for url in urls:
                        url = url.replace('\n', '')
                        base_filename = url.split('/')[-1]
                        output_file = f"{output_dir}/{base_filename}.json"
                        self.generate_files(url, output_file)
                        self.run_command()
                messagebox.showinfo("Success", f"Crawling data successfully, your data is saved in the output directory {output_dir}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            output_file = filedialog.asksaveasfilename(title="Save File As", defaultextension=".json", filetypes=[("JSON files", "*.json")])
            self.generate_files(url, output_file)
            self.run_command()
            messagebox.showinfo("Success", f"Crawling data successfully, your data is saved in the output directory {output_file}")
        self.crawl_button.configure(state=ctk.NORMAL)
    
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
        _, stderr = p.communicate()
        if stderr is not None:
            filepath = "generate.sh"
            p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
            _, stderr = p.communicate()
            if stderr is not None:
                return False
        return True

if __name__ == "__main__":
    downloader = GUI()
    downloader.run()