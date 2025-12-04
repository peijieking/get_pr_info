const { test, expect } = require('@playwright/test');

test('页面加载并显示标题', async ({ page }) => {
  await page.goto('http://localhost:46637');
  await expect(page).toHaveTitle('GitHub PR 获取工具');
  await expect(page.locator('.header h1')).toHaveText('GitHub PR 获取工具');
});

test('关键按钮存在且可见', async ({ page }) => {
  await page.goto('http://localhost:46637');
  const fetchBtn = page.locator('#fetchBtn');
  await expect(fetchBtn).toBeVisible();
  await expect(fetchBtn).toHaveText('获取 PR 信息');
});

test('输入框存在且有默认值', async ({ page }) => {
  await page.goto('http://localhost:46637');
  const repoUrlInput = page.locator('#repoUrl');
  await expect(repoUrlInput).toBeVisible();
  await expect(repoUrlInput).toHaveValue('https://github.com/facebook/react');
});

test('点击按钮后显示加载状态', async ({ page }) => {
  await page.goto('http://localhost:46637');
  const fetchBtn = page.locator('#fetchBtn');
  const statusDiv = page.locator('#status');
  
  // 点击按钮
  await fetchBtn.click();
  
  // 检查加载状态
  await expect(statusDiv).toHaveClass(/loading/);
  await expect(statusDiv).toHaveText('正在获取 PR 信息...');
  await expect(fetchBtn).toBeDisabled();
});

test('Enter 键可以触发获取功能', async ({ page }) => {
  await page.goto('http://localhost:46637');
  const repoUrlInput = page.locator('#repoUrl');
  const statusDiv = page.locator('#status');
  
  // 输入仓库地址并按 Enter
  await repoUrlInput.fill('https://github.com/facebook/react');
  await repoUrlInput.press('Enter');
  
  // 检查加载状态
  await expect(statusDiv).toHaveClass(/loading/);
});