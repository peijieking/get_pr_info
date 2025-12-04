const { test, expect } = require('@playwright/test');

test('页面加载测试', async ({ page }) => {
  // 导航到应用页面
  await page.goto('http://localhost:53573');

  // 检查页面标题
  await expect(page).toHaveTitle('GitHub PR 信息获取器');

  // 检查页面主标题
  await expect(page.locator('h1')).toHaveText('GitHub PR 信息获取器');

  // 检查副标题
  await expect(page.locator('.subtitle')).toHaveText('输入 GitHub 仓库地址，获取所有开放状态的 Pull Requests 信息');
});

test('输入框和按钮存在测试', async ({ page }) => {
  // 导航到应用页面
  await page.goto('http://localhost:53573');

  // 检查输入框存在
  const input = page.locator('#repoUrl');
  await expect(input).toBeVisible();
  await expect(input).toHaveAttribute('placeholder', '例如: https://github.com/microsoft/vscode');

  // 检查按钮存在
  const button = page.locator('#fetchBtn');
  await expect(button).toBeVisible();
  await expect(button).toHaveText('获取 PR 信息');
});

test('输出区域存在测试', async ({ page }) => {
  // 导航到应用页面
  await page.goto('http://localhost:53573');

  // 检查输出区域存在
  const output = page.locator('#output');
  await expect(output).toBeVisible();
  await expect(output).toHaveText('请输入仓库地址并点击"获取 PR 信息"按钮开始...');
});

test('Enter 键触发功能测试', async ({ page }) => {
  // 导航到应用页面
  await page.goto('http://localhost:53573');

  // 输入仓库地址并按 Enter 键
  const input = page.locator('#repoUrl');
  await input.fill('https://github.com/microsoft/vscode');
  await input.press('Enter');

  // 检查按钮是否显示加载状态
  const button = page.locator('#fetchBtn');
  await expect(button).toBeDisabled();
  await expect(button).toContainText('获取中...');
});