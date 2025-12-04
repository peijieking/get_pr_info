import tkinter as tk
from tkinter import ttk, scrolledtext
import requests

def get_pr_info():
    # 清空滚动文本框
    pr_text.delete('1.0', tk.END)
    
    # 从输入框中获取仓库地址
    repo_url = repo_entry.get().strip()
    
    if not repo_url:
        pr_text.insert(tk.END, "错误：请输入GitHub仓库地址")
        return
    
    # 解析仓库地址以获取所有者和仓库名称
    # 支持的格式：https://github.com/owner/repo 或 github.com/owner/repo
    try:
        if repo_url.startswith('https://'):
            repo_url = repo_url[8:]
        elif repo_url.startswith('http://'):
            repo_url = repo_url[7:]
        
        # 分割URL以获取所有者和仓库名称
        parts = repo_url.split('/')
        if len(parts) < 3:
            raise ValueError("无效的仓库地址")
        
        owner = parts[1]
        repo = parts[2]
        
        # 移除仓库名称后的任何额外路径或参数
        if '/' in repo:
            repo = repo.split('/')[0]
        if '?' in repo:
            repo = repo.split('?')[0]
    except Exception as e:
        pr_text.insert(tk.END, f"错误：无法解析仓库地址 - {str(e)}")
        return
    
    # 调用GitHub API获取open状态的PR信息
    api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=open"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # 如果响应状态不是200，会引发HTTPError
        
        prs = response.json()
        
        if not prs:
            pr_text.insert(tk.END, "没有找到open状态的PR")
            return
        
        # 解析PR信息并显示在滚动文本框中
        for i, pr in enumerate(prs, 1):
            pr_text.insert(tk.END, f"PR #{i}:\n")
            pr_text.insert(tk.END, f"  标题: {pr['title']}\n")
            pr_text.insert(tk.END, f"  分支: {pr['head']['ref']} -> {pr['base']['ref']}\n")
            pr_text.insert(tk.END, f"  网址: {pr['html_url']}\n")
            pr_text.insert(tk.END, "\n")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            pr_text.insert(tk.END, "错误：仓库不存在或无法访问")
        else:
            pr_text.insert(tk.END, f"错误：HTTP请求失败 - {str(e)}")
    except requests.exceptions.ConnectionError:
        pr_text.insert(tk.END, "错误：网络连接失败，请检查网络设置")
    except requests.exceptions.Timeout:
        pr_text.insert(tk.END, "错误：请求超时")
    except requests.exceptions.RequestException as e:
        pr_text.insert(tk.END, f"错误：请求失败 - {str(e)}")
    except Exception as e:
        pr_text.insert(tk.END, f"错误：未知错误 - {str(e)}")

# 创建主窗口
root = tk.Tk()
root.title("GitHub PR信息查看器")
root.geometry("800x600")  # 增大界面尺寸

# 创建顶部框架用于放置标签、输入框和按钮
top_frame = ttk.Frame(root)
top_frame.pack(fill=tk.X, padx=20, pady=20)

# 使用grid布局管理器来控制标签、输入框和按钮的位置
# 设置列权重，使得输入框可以横向扩展
top_frame.columnconfigure(1, weight=1)

# 创建仓库地址标签
repo_label = ttk.Label(top_frame, text="GitHub仓库地址:")
repo_label.grid(row=0, column=0, padx=(0, 10), pady=5, sticky=tk.W)

# 创建仓库地址输入框，不设置固定宽度，这样可以横向扩展
repo_entry = ttk.Entry(top_frame)
repo_entry.grid(row=0, column=1, padx=(0, 10), pady=5, sticky=tk.EW)

# 创建获取PR信息按钮
fetch_button = ttk.Button(top_frame, text="获取PR信息", command=get_pr_info)
fetch_button.grid(row=0, column=2, pady=5, sticky=tk.W)

# 创建底部框架用于放置滚动文本框
bottom_frame = ttk.Frame(root)
bottom_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

# 创建滚动文本框，增大宽度使得一行显示更多文字
pr_text = scrolledtext.ScrolledText(bottom_frame, width=90, height=25)
pr_text.pack(fill=tk.BOTH, expand=True)

# 启动主循环
root.mainloop()