#!/usr/bin/env python3
import os
import requests
import re

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
USERNAME = 'shimu-ui'

def get_repos():
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'
    
    url = f"https://api.github.com/users/{USERNAME}/repos"
    params = {'sort': 'updated', 'per_page': 8, 'type': 'owner'}
    
    response = requests.get(url, headers=headers, params=params)
    repos = response.json()
    
    # 过滤仓库
    filtered = []
    for repo in repos:
        # 基本过滤条件
        if (not repo['fork'] and repo['name'] != USERNAME and 
            not repo['name'].endswith('.github.io') and repo['size'] > 0):
            
            # 过滤测试项目
            repo_name = repo['name'].lower()
            if is_test_project(repo_name):
                print(f"🚫 跳过测试项目: {repo['name']}")
                continue
                
            filtered.append(repo)
    
    return filtered[:8]

def is_test_project(repo_name):
    """判断是否为测试项目"""
    # 纯数字项目（如 "2", "123", "test1" 等）
    if repo_name.isdigit() or (repo_name.startswith('test') and repo_name[4:].isdigit()):
        return True
    
    # 常见的测试项目名称模式
    test_patterns = [
        'test', 'demo', 'example', 'sample', 'temp', 'tmp', 'backup',
        'old', 'new', 'v1', 'v2', 'version1', 'version2',
        'dev', 'development', 'staging', 'beta', 'alpha'
    ]
    
    for pattern in test_patterns:
        if pattern in repo_name:
            return True
    
    # 过短的项目名（少于3个字符）
    if len(repo_name) < 3:
        return True
    
    return False

def get_tech_badges(repo):
    tech_map = {
        'javascript': '![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)',
        'python': '![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)',
        'vue': '![Vue.js](https://img.shields.io/badge/Vue.js-42B883?style=flat&logo=vue.js&logoColor=white)',
        'react': '![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)',
        'node': '![Node.js](https://img.shields.io/badge/Node.js-6DB33F?style=flat&logo=node.js&logoColor=white)',
        'solidity': '![Solidity](https://img.shields.io/badge/Solidity-363636?style=flat&logo=solidity&logoColor=white)',
        'ethereum': '![Ethereum](https://img.shields.io/badge/Ethereum-627EEA?style=flat&logo=ethereum&logoColor=white)',
        'spring': '![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=flat&logo=spring-boot&logoColor=white)',
        'wechat': '![微信小程序](https://img.shields.io/badge/微信小程序-07C160?style=flat&logo=wechat&logoColor=white)',
        'ar': '![AR技术](https://img.shields.io/badge/AR技术-FF6B6B?style=flat&logo=unity&logoColor=white)',
        'ai': '![AI技术](https://img.shields.io/badge/AI技术-FF6F00?style=flat&logo=tensorflow&logoColor=white)',
        'blockchain': '![区块链](https://img.shields.io/badge/区块链-627EEA?style=flat&logo=ethereum&logoColor=white)',
        'postgresql': '![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)',
        'mysql': '![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)',
        'mongodb': '![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)',
        'docker': '![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)',
        'aws': '![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat&logo=amazonaws&logoColor=white)',
        'vercel': '![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white)',
    }
    
    badges = []
    description = repo.get('description', '') or ''
    name_desc = f"{repo['name']} {description}".lower()
    
    # 根据语言
    if repo.get('language'):
        lang = repo['language'].lower()
        if lang in tech_map:
            badges.append(tech_map[lang])
    
    # 根据名称和描述
    for tech, badge in tech_map.items():
        if tech in name_desc and badge not in badges:
            badges.append(badge)
    
    return badges[:3]

def get_project_readme_content(repo_name):
    """获取项目的README内容"""
    try:
        # 尝试获取项目的README文件内容
        url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/readme"
        headers = {'Accept': 'application/vnd.github.v3+json'}
        if GITHUB_TOKEN:
            headers['Authorization'] = f'token {GITHUB_TOKEN}'
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            readme_data = response.json()
            import base64
            content = base64.b64decode(readme_data['content']).decode('utf-8')
            return content
    except Exception as e:
        print(f"获取 {repo_name} 的README失败: {e}")
    
    return None

def extract_description_from_readme(readme_content):
    """从README内容中提取简洁描述"""
    if not readme_content:
        return None
    
    lines = readme_content.split('\n')
    
    # 首先尝试找到HTML段落中的描述
    for line in lines:
        line = line.strip()
        if not line or line.startswith('![') or line.startswith('['):
            continue
        
        # 处理HTML段落标签 - 优先提取描述性内容
        if '<p>' in line and '</p>' in line:
            match = re.search(r'<p>(.*?)</p>', line)
            if match:
                content = match.group(1)
                # 移除HTML标签
                content = re.sub(r'<[^>]+>', '', content)
                # 检查是否是描述性内容
                if (len(content) > 10 and len(content) < 150 and 
                    ('Windows' in content or '弹窗' in content or '识别' in content or
                     '一个' in content or '强大的' in content or '解决方案' in content)):
                    return content
    
    # 然后尝试找到普通文本中的描述
    for line in lines:
        line = line.strip()
        if not line or line.startswith('![') or line.startswith('[') or line.startswith('<') or line.startswith('#'):
            continue
        
        # 移除markdown标记
        clean_line = re.sub(r'[#*`\[\]()]', '', line).strip()
        # 检查是否是描述性内容
        if (len(clean_line) > 10 and len(clean_line) < 150 and
            ('一个' in clean_line or '强大的' in clean_line or '解决方案' in clean_line or
             '系统' in clean_line or '平台' in clean_line or '应用' in clean_line or
             'Windows' in clean_line or '弹窗' in clean_line or '识别' in clean_line)):
            return clean_line
    
    # 最后尝试找到标题作为备选
    for line in lines:
        line = line.strip()
        if not line or line.startswith('![') or line.startswith('['):
            continue
        
        # 处理HTML标题标签
        if line.startswith('<h') and '>' in line:
            match = re.search(r'<h[^>]*>(.*?)</h[^>]*>', line)
            if match:
                content = match.group(1)
                if len(content) > 5 and len(content) < 100:
                    return content
        
        # 处理markdown标题
        if line.startswith('# ') and len(line) > 3:
            content = line[2:].strip()
            if len(content) > 5 and len(content) < 100:
                return content
    
    return None

def get_description(repo):
    """获取项目描述，优先从README文件获取"""
    repo_name = repo['name']
    
    # 首先尝试从README文件获取描述
    readme_content = get_project_readme_content(repo_name)
    if readme_content:
        description = extract_description_from_readme(readme_content)
        if description:
            return description
    
    # 如果无法获取README，使用GitHub API的description
    github_description = repo.get('description', '') or ''
    if github_description:
        return github_description
    
    # 最后使用默认描述
    desc_map = {
        'blog': '📝 个人博客系统，支持动态内容管理和 🎭 Live2D 看板娘集成',
        'blockchain': '⛓️ 基于区块链技术的去中心化应用，采用智能合约实现',
        'certificate': '🔗 数字证书系统，确保数据安全和身份验证',
        'supply': '🌿 供应链溯源平台，实现从源头到终端的全流程透明化管理',
        'tourism': '🏮 文旅助农小程序，融合AR、AI等前沿技术助力乡村振兴',
        'ai': '🤖 AI智能应用，集成机器学习和深度学习技术',
        'web3': '🌐 Web3应用，探索去中心化互联网的未来',
        'miniprogram': '📱 微信小程序，提供便捷的移动端服务体验',
        'api': '🔌 API服务，提供稳定可靠的后端接口服务',
        'tool': '🛠️ 开发工具，提升开发效率和代码质量',
        'game': '🎮 游戏应用，融合创新技术和娱乐体验',
        'default': '🚀 创新项目，融合前沿技术解决实际问题'
    }
    
    name = repo_name.lower()
    for project_type, desc in desc_map.items():
        if project_type in name:
            return desc
    
    return desc_map['default']

def extract_existing_repos(content):
    """从README内容中提取已存在的项目名称"""
    import re
    
    # 匹配GitHub Readme Card链接中的repo参数
    pattern = r'repo=([^&]+)'
    matches = re.findall(pattern, content)
    
    # 去重并返回
    existing_repos = list(set(matches))
    print(f"🔍 从README中提取到 {len(existing_repos)} 个已存在项目")
    
    return existing_repos

def get_daily_quote():
    """获取每日名言"""
    try:
        # 使用luckycola API
        url = 'https://luckycola.com.cn/tools/yiyan'
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        data = {
            'ColaKey': 'Siky6pcl1qJe2S1756534912492G0FUlJ3Hj6'
        }
        
        response = requests.post(url, json=data, headers=headers, timeout=30)
        if response.status_code == 200:
            result = response.json()
            if result.get('code') == 0 and 'data' in result:
                # 优先返回中文名言
                if result['data'].get('note'):
                    return result['data']['note']
                # 如果没有中文，返回英文
                elif result['data'].get('content'):
                    return result['data']['content']
    except Exception as e:
        print(f"获取名言API失败: {e}")
    
    # 备用名言
    quotes = [
        "代码改变世界，技术连接未来",
        "学如逆水行舟，不进则退",
        "实践是检验真理的唯一标准",
        "创新是发展的第一动力",
        "千里之行，始于足下",
        "业精于勤，荒于嬉"
    ]
    import random
    return random.choice(quotes)

def get_chinese_joke():
    """获取中文笑话"""
    try:
        response = requests.get('https://api.vvhan.com/api/joke', timeout=10)
        if response.status_code == 200:
            result = response.json()
            if result.get('success') and 'data' in result:
                return result['data']
    except Exception as e:
        print(f"获取笑话API失败: {e}")
    
    # 备用笑话
    jokes = [
        "程序员最讨厌康熙，因为康熙老是留胡子。",
        "为什么程序员总是分不清万圣节和圣诞节？因为 Oct 31 == Dec 25。",
        "一个程序员去超市买东西，妻子说：买个面包，如果看到鸡蛋就买十个。他回来后带了十个面包。",
        "为什么程序员不喜欢户外活动？因为有太多的bug。",
        "程序员的女朋友对他说：去超市帮我买一瓶牛奶，如果看到鸡蛋就买六个。他回来后带了六瓶牛奶。"
    ]
    import random
    return random.choice(jokes)

def format_project(repo):
    tech_badges = get_tech_badges(repo)
    description = get_description(repo)
    
    # 选择emoji
    emoji = "🚀"
    if 'blog' in repo['name'].lower():
        emoji = "📝"
    elif 'blockchain' in repo['name'].lower():
        emoji = "⛓️"
    elif 'ai' in repo['name'].lower():
        emoji = "🤖"
    elif 'game' in repo['name'].lower():
        emoji = "🎮"
    elif 'app' in repo['name'].lower():
        emoji = "📱"
    
    project_name = repo['name'].replace('-', ' ').replace('_', ' ').title()
    
    card = f"""**{emoji} {project_name}**

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username={USERNAME}&repo={repo['name']}&theme=radical&hide_border=true&bg_color=0D1117&title_color=6CF&text_color=FFFFFF&icon_color=6CF)](https://github.com/{USERNAME}/{repo['name']})

"""
    
    for badge in tech_badges:
        card += f"{badge}\n"
    
    card += f"\n{description}\n"
    
    return card

def update_daily_quote(content):
    """更新每日名言部分"""
    quote = get_daily_quote()
    
    # 查找每日一句部分
    start_marker = "## 💡 每日一句"
    end_marker = "---"
    
    start_pos = content.find(start_marker)
    if start_pos == -1:
        print("未找到每日一句部分")
        return content
    
    # 找到结束位置
    end_pos = content.find(end_marker, start_pos)
    if end_pos == -1:
        end_pos = content.find('\n\n', start_pos)
    
    # 构建新的每日一句内容
    new_quote_section = f"""## 💡 每日一句

<div align="center">

> *"{quote}"* ✨

</div>

---"""
    
    # 替换内容
    updated_content = content[:start_pos] + new_quote_section + content[end_pos:]
    
    print(f"💬 更新每日名言: {quote}")
    return updated_content

def update_chinese_joke(content):
    """更新中文笑话部分"""
    joke = get_chinese_joke()
    
    # 查找有趣的事实部分
    start_marker = "## 🌈 有趣的事实"
    end_marker = "---"
    
    start_pos = content.find(start_marker)
    if start_pos == -1:
        print("未找到有趣的事实部分")
        return content
    
    # 找到结束位置
    end_pos = content.find(end_marker, start_pos)
    if end_pos == -1:
        end_pos = content.find('\n\n', start_pos)
    
    # 构建新的有趣的事实内容
    new_joke_section = f"""## 🌈 有趣的事实

<div align="center">

### 🎭 关于我的一些趣事

</div>

- 🎮 **游戏爱好者**: 热爱策略游戏和独立游戏，它们激发我的创造力
- 🍕 **代码与美食**: 边写代码边品尝世界各地的美食是我的最爱
- 🌙 **夜猫子程序员**: 最佳编程时间是晚上10点到凌晨2点
- 📖 **技术书虫**: 每月至少阅读2本技术书籍和1本非技术书籍
- 🎵 **代码配乐**: 编程时喜欢听爵士乐和电子音乐
- 🏃‍♂️ **运动健身**: 每周至少跑步3次，保持身心健康

<div align="center">

> *"🎭 {joke}"* 😄

</div>

---"""
    
    # 替换内容
    updated_content = content[:start_pos] + new_joke_section + content[end_pos:]
    
    print(f"😄 更新中文笑话: {joke}")
    return updated_content

def update_readme():
    repos = get_repos()
    
    # 从上级目录读取README.md
    readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新每日名言和中文笑话
    content = update_daily_quote(content)
    content = update_chinese_joke(content)
    
    start_marker = "## 🎯 精选项目"
    end_marker = "## 🌟 技能与专长"
    
    start_pos = content.find(start_marker)
    end_pos = content.find(end_marker)
    
    if start_pos == -1 or end_pos == -1:
        print("未找到精选项目部分")
        return
    
    # 从README中提取已存在的项目
    existing_repos = extract_existing_repos(content[start_pos:end_pos])
    print(f"📋 当前精选项目: {existing_repos}")
    
    # 检查是否有新项目需要添加
    new_repos = []
    
    for repo in repos:
        if repo['name'] not in existing_repos:
            new_repos.append(repo)
    
    if not new_repos:
        print("✅ 没有新的项目需要添加，保持现有精选项目")
        # 即使没有新项目，也要保存每日名言的更新
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return
    
    print(f"📦 发现 {len(new_repos)} 个新项目，准备添加到精选项目")
    
    # 保留现有内容，只添加新项目
    existing_content = content[start_pos:end_pos]
    
    # 找到表格的结束位置
    table_end = existing_content.rfind('</table>')
    if table_end == -1:
        print("未找到项目表格，无法添加新项目")
        return
    
    # 在表格结束前添加新项目
    new_projects_html = ""
    for i in range(0, len(new_repos), 2):
        new_projects_html += "<tr>\n"
        
        if i < len(new_repos):
            new_projects_html += f'<td width="50%" align="center">\n\n'
            new_projects_html += format_project(new_repos[i])
            new_projects_html += "\n</td>\n"
        
        if i + 1 < len(new_repos):
            new_projects_html += f'<td width="50%" align="center">\n\n'
            new_projects_html += format_project(new_repos[i + 1])
            new_projects_html += "\n</td>\n"
        else:
            new_projects_html += '<td width="50%" align="center">\n\n</td>\n'
        
        new_projects_html += "</tr>\n"
    
    # 在表格结束前插入新项目
    updated_content = (
        existing_content[:table_end] + 
        new_projects_html + 
        existing_content[table_end:]
    )
    
    # 更新整个内容
    final_content = content[:start_pos] + updated_content + content[end_pos:]
    
    # 写回到上级目录的README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"✅ 成功添加了 {len(new_repos)} 个新项目到精选项目")

if __name__ == "__main__":
    update_readme()
