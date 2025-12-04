# GitHub PR 获取工具

一个简单易用的网页应用，用于获取 GitHub 仓库的 Pull Requests 信息。

## 功能特性

- 📝 **输入仓库地址**：支持输入 GitHub 仓库的 URL
- 🚀 **一键获取**：点击按钮即可获取所有开放的 PR 信息
- 📋 **详细信息**：显示 PR 标题、分支名称和 PR 网址
- 🎨 **现代 UI**：美观的界面设计，响应式布局
- ⚡ **实时状态**：显示加载、成功和错误状态
- 🔍 **链接跳转**：点击 PR 链接可直接跳转到 GitHub 页面

## 技术栈

- HTML5
- CSS3
- JavaScript (ES6+)
- Playwright (测试)

## 快速开始

### 1. 安装依赖

```bash
npm install
```

### 2. 启动开发服务器

```bash
npm run dev
```

服务器将在 `http://localhost:46637` 启动

### 3. 访问应用

在浏览器中打开 `http://localhost:46637`

### 4. 使用方法

1. 在输入框中输入 GitHub 仓库地址（例如：`https://github.com/facebook/react`）
2. 点击「获取 PR 信息」按钮或按 Enter 键
3. 等待加载完成，查看 PR 信息

## 生产构建

```bash
npm run build
```

构建产物将生成在 `build/` 目录中

## 测试

### 1. 安装 Playwright 浏览器

```bash
npx playwright install
```

### 2. 运行测试

```bash
npm test
```

## 项目结构

```
github-pr-fetcher/
├─ build/                # 生产构建产物
├─ tests/                # Playwright 测试文件
│  └─ pr-fetcher.spec.js # 测试脚本
├─ index.html            # 主应用文件
├─ package.json          # 项目配置
├─ playwright.config.js  # Playwright 配置
└─ README.md             # 项目文档
```

## API 使用

该应用使用 GitHub API 获取 PR 信息：

```
GET https://api.github.com/repos/{owner}/{repo}/pulls?state=open&per_page=100
```

注意：GitHub API 有请求限制，未认证用户每小时最多 60 次请求。

## 浏览器支持

- Chrome (推荐)
- Firefox
- Safari
- Edge

## License

MIT