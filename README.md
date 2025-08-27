---
title: "👋 关于 shimu-ui"
---

## 嘿，你好！我是 shimu-ui ✨

非常高兴能在这里与你相遇！我是一个充满好奇心的**全栈开发者** 🚀，热衷于探索技术的前沿领域，并将所学转化为实用的解决方案。

建立这个小站，主要是想用它来**分享我的技术心得** 📚，并**记录下学习过程中的点点滴滴** ✍️。如果我的文字能给你带来一丁点启发或者帮助，那将是我莫大的荣幸！

---

### 🛠️ 技术栈概览

<div style="text-align: center; margin: 40px 0 20px 0;">
  <h3 style="color: #6cf; font-size: 24px; margin-bottom: 10px;">💫 我的技术栈</h3>
  <p style="color: #888; font-size: 14px; margin: 0;"></p>
</div>

<div id="tech-3d-container" style="width: 100%; height: 500px; position: relative; margin: 30px 0; background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%); border-radius: 16px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.3);">
  <canvas id="tech-canvas" style="width: 100%; height: 100%;"></canvas>
  
  <div id="tech-info" style="position: absolute; top: 30px; left: 30px; color: #ffffff; font-size: 14px; pointer-events: none; opacity: 0; transition: all 0.3s ease; background: rgba(0,0,0,0.8); padding: 15px; border-radius: 10px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1);">
    <div id="tech-name" style="font-weight: bold; font-size: 16px; margin-bottom: 5px; color: #6cf;"></div>
    <div id="tech-desc" style="color: #cccccc;"></div>
  </div>
  
  <div style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); color: #888; font-size: 12px; text-align: center;">
    <div>🖱️ 悬停查看技术详情</div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(function() {
  const container = document.getElementById('tech-3d-container');
  const canvas = document.getElementById('tech-canvas');
  const info = document.getElementById('tech-info');
  const techName = document.getElementById('tech-name');
  const techDesc = document.getElementById('tech-desc');

  // 技术栈数据 - 可爱emoji版本
  const techStack = [
    { name: 'Node.js', category: 'backend', color: '#6db33f', desc: 'JavaScript 运行时环境', level: 90, emoji: '🟢' },
    { name: 'Express.js', category: 'backend', color: '#ffffff', desc: 'Web 应用框架', level: 85, emoji: '⚡' },
    { name: 'Flask', category: 'backend', color: '#000000', desc: 'Python Web 框架', level: 80, emoji: '🌶️' },
    { name: 'Socket.IO', category: 'backend', color: '#010101', desc: '实时通信库', level: 75, emoji: '🔌' },
    { name: 'Vue.js', category: 'frontend', color: '#42b883', desc: '渐进式 JavaScript 框架', level: 90, emoji: '💚' },
    { name: 'React', category: 'frontend', color: '#61dafb', desc: '用户界面构建库', level: 85, emoji: '⚛️' },
    { name: '微信小程序', category: 'mobile', color: '#07c160', desc: '移动应用开发', level: 85, emoji: '📱' },
    { name: 'uni-app', category: 'mobile', color: '#ff6b35', desc: '跨平台开发框架', level: 80, emoji: '🔄' },
    { name: 'Python', category: 'language', color: '#3776ab', desc: '高级编程语言', level: 90, emoji: '🐍' },
    { name: 'Java', category: 'language', color: '#ed8b00', desc: '面向对象编程语言', level: 85, emoji: '☕' },
    { name: 'Solidity', category: 'blockchain', color: '#363636', desc: '智能合约编程语言', level: 80, emoji: '🔗' },
    { name: 'Ethereum', category: 'blockchain', color: '#627eea', desc: '区块链平台', level: 75, emoji: '⛓️' },
    { name: 'AR技术', category: 'ai', color: '#ff6b6b', desc: '增强现实技术', level: 70, emoji: '👁️' },
    { name: 'AI客服', category: 'ai', color: '#4ecdc4', desc: '人工智能应用', level: 75, emoji: '🤖' },
    { name: 'OpenCV', category: 'ai', color: '#5c3ee8', desc: '计算机视觉库', level: 70, emoji: '📷' },
    { name: 'PostgreSQL', category: 'database', color: '#336791', desc: '关系型数据库', level: 85, emoji: '🐘' },
    { name: 'MongoDB', category: 'database', color: '#47a248', desc: '文档数据库', level: 80, emoji: '🍃' },
    { name: 'MySQL', category: 'database', color: '#4479a1', desc: '关系型数据库', level: 85, emoji: '🐬' },
    { name: 'Vercel', category: 'cloud', color: '#000000', desc: '云部署平台', level: 90, emoji: '🚀' },
    { name: 'Neon', category: 'cloud', color: '#00d4aa', desc: 'Serverless Postgres', level: 85, emoji: '🟢' },
    { name: '阿里云', category: 'cloud', color: '#ff6a00', desc: '云计算平台', level: 80, emoji: '☁️' },
    { name: 'Docker', category: 'devops', color: '#2496ed', desc: '容器化平台', level: 75, emoji: '🐳' },
    { name: 'Rust', category: 'language', color: '#ce422b', desc: '系统编程语言', level: 60, emoji: '🦀' }
  ];

  // Three.js 设置
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
  
  renderer.setSize(container.clientWidth, container.clientHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // 创建技术栈球体
  const spheres = [];
  const sphereGeometry = new THREE.SphereGeometry(0.3, 16, 16);

  techStack.forEach((tech, index) => {
    // 根据技能熟练度调整大小
    const size = 1.2 + (tech.level / 100) * 1.8; // 1.2-3.0 范围
    
    // 创建emoji文本精灵
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.width = 128;
    canvas.height = 128;
    
    // 设置背景圆形
    context.beginPath();
    context.arc(64, 64, 60, 0, Math.PI * 2);
    context.fillStyle = tech.color;
    context.fill();
    
    // 添加发光效果
    context.shadowColor = tech.color;
    context.shadowBlur = 20;
    context.fill();
    
    // 绘制emoji
    context.font = '60px Arial';
    context.textAlign = 'center';
    context.textBaseline = 'middle';
    context.shadowBlur = 0;
    context.fillText(tech.emoji, 64, 64);
    
    // 创建纹理和材质
    const texture = new THREE.CanvasTexture(canvas);
    const material = new THREE.SpriteMaterial({ 
      map: texture,
      transparent: true,
      opacity: 0.9
    });
    
    const sprite = new THREE.Sprite(material);
    sprite.scale.set(size, size, 1);
    
    // 创建螺旋分布
    const angle = (index / techStack.length) * Math.PI * 4;
    const radius = 6 + Math.sin(angle * 3) * 3;
    const height = Math.cos(angle * 2) * 3 + Math.sin(angle * 4) * 1;
    
    sprite.position.x = Math.cos(angle) * radius;
    sprite.position.y = height;
    sprite.position.z = Math.sin(angle) * radius;
    
    sprite.userData = tech;
    spheres.push(sprite);
    scene.add(sprite);
    
    // 移除光环效果，保持简洁
  });

  // 添加动态连接线（箭头效果）
  const lineMaterial = new THREE.LineBasicMaterial({ 
    color: 0x4facfe, 
    transparent: true, 
    opacity: 0.4,
    linewidth: 2
  });

  // 创建螺旋箭头连接
  for (let i = 0; i < spheres.length; i++) {
    const next = spheres[(i + 2) % spheres.length]; // 跳过相邻，连接间隔的球体
    const current = spheres[i];
    
    // 创建曲线路径
    const curve = new THREE.CubicBezierCurve3(
      current.position,
      new THREE.Vector3(
        (current.position.x + next.position.x) / 2 + Math.sin(i) * 2,
        (current.position.y + next.position.y) / 2 + Math.cos(i) * 2,
        (current.position.z + next.position.z) / 2
      ),
      new THREE.Vector3(
        (current.position.x + next.position.x) / 2 - Math.sin(i) * 2,
        (current.position.y + next.position.y) / 2 - Math.cos(i) * 2,
        (current.position.z + next.position.z) / 2
      ),
      next.position
    );
    
    const points = curve.getPoints(50);
    const geometry = new THREE.BufferGeometry().setFromPoints(points);
    const line = new THREE.Line(geometry, lineMaterial);
    scene.add(line);
  }

  // 光照系统
  const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
  scene.add(ambientLight);

  const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
  directionalLight.position.set(10, 10, 5);
  scene.add(directionalLight);

  camera.position.z = 15;

  // 添加粒子效果
  const particleCount = 100;
  const particles = new THREE.BufferGeometry();
  const particlePositions = new Float32Array(particleCount * 3);
  const particleColors = new Float32Array(particleCount * 3);

  for (let i = 0; i < particleCount; i++) {
    const i3 = i * 3;
    particlePositions[i3] = (Math.random() - 0.5) * 20;
    particlePositions[i3 + 1] = (Math.random() - 0.5) * 20;
    particlePositions[i3 + 2] = (Math.random() - 0.5) * 20;
    
    particleColors[i3] = Math.random() * 0.5 + 0.5;
    particleColors[i3 + 1] = Math.random() * 0.5 + 0.5;
    particleColors[i3 + 2] = Math.random() * 0.5 + 0.5;
  }

  particles.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));
  particles.setAttribute('color', new THREE.BufferAttribute(particleColors, 3));

  const particleMaterial = new THREE.PointsMaterial({
    size: 0.1,
    transparent: true,
    opacity: 0.6,
    vertexColors: true,
    blending: THREE.AdditiveBlending
  });

  const particleSystem = new THREE.Points(particles, particleMaterial);
  scene.add(particleSystem);

  // 动画
  let time = 0;
  function animate() {
    requestAnimationFrame(animate);
    time += 0.002; // 降低动画速度

    // emoji精灵动态浮动
    spheres.forEach((sprite, index) => {
      // 轻微的旋转动画
      sprite.rotation.z += 0.01 + Math.sin(time + index) * 0.005;
      
      // 轻微浮动效果
      sprite.position.y += Math.sin(time * 2 + index * 0.5) * 0.002;
      
      // 螺旋轨道运动
      const angle = (index / spheres.length) * Math.PI * 4 + time * 0.4;
      const radius = 6 + Math.sin(angle * 3) * 3;
      const height = Math.cos(angle * 2) * 3 + Math.sin(angle * 4) * 1;
      
      sprite.position.x = Math.cos(angle) * radius;
      sprite.position.z = Math.sin(angle) * radius;
      sprite.position.y = height;
      
      // 轻微缩放效果
      const scale = 1 + Math.sin(time * 1.5 + index) * 0.05;
      sprite.scale.set(scale, scale, 1);
    });

    // 相机动态移动
    camera.position.x = Math.sin(time * 0.3) * 3;
    camera.position.y = Math.cos(time * 0.25) * 2;
    camera.position.z = 15 + Math.sin(time * 0.1) * 1;
    camera.lookAt(0, 0, 0);

    // 粒子动画
    const positions = particleSystem.geometry.attributes.position.array;
    for (let i = 0; i < particleCount; i++) {
      const i3 = i * 3;
      positions[i3] += Math.sin(time + i) * 0.01;
      positions[i3 + 1] += Math.cos(time + i) * 0.01;
      positions[i3 + 2] += Math.sin(time * 0.5 + i) * 0.01;
    }
    particleSystem.geometry.attributes.position.needsUpdate = true;

    renderer.render(scene, camera);
  }

  // 鼠标交互
  const raycaster = new THREE.Raycaster();
  const mouse = new THREE.Vector2();

  function onMouseMove(event) {
    const rect = canvas.getBoundingClientRect();
    mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
    mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(spheres);

    if (intersects.length > 0) {
      const sprite = intersects[0].object;
      sprite.scale.setScalar(1.5);
      sprite.material.opacity = 1;
      
      // 显示技术信息
      techName.textContent = `${sprite.userData.emoji} ${sprite.userData.name}`;
      techDesc.textContent = `${sprite.userData.desc} | 熟练度: ${sprite.userData.level}%`;
      info.style.opacity = 1;
      info.style.transform = 'translateY(0)';
    } else {
      spheres.forEach(sprite => {
        const scale = 1 + Math.sin(time * 1.5 + spheres.indexOf(sprite)) * 0.05;
        sprite.scale.set(scale, scale, 1);
        sprite.material.opacity = 0.9;
      });
      info.style.opacity = 0;
      info.style.transform = 'translateY(-10px)';
    }
  }

  canvas.addEventListener('mousemove', onMouseMove);

  // 响应式
  window.addEventListener('resize', () => {
    camera.aspect = container.clientWidth / container.clientHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(container.clientWidth, container.clientHeight);
  });

  animate();
})();
</script>

---

### 💻 技术栈与工具箱

我对计算机的世界充满了无限的热情 🔥，尤其喜欢钻研和实践以下技术。以下是我的技术能力概览：

<div style="text-align: center; margin: 20px 0;">
  <div style="display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 10px 20px; border-radius: 25px; color: white; font-weight: bold; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
    🎯 全栈开发 | 🚀 6个完整项目 | ⚡ 持续学习中
  </div>
</div>

#### 🚀 后端技术
* **编程语言**: 🐍 Python, ☕ Java, ⚙️ C, 🔷 C#, 🦀 Rust
* **Web 框架**: 🟢 Node.js, ⚡ Express.js, 🍃 Spring Boot, 🌶️ Flask
* **实时通信**: 🔌 Socket.IO, 📡 WebSocket
* **数据库**: 🐘 PostgreSQL, 🍃 MongoDB, 🐬 MySQL

#### 🎨 前端技术
* **核心语言**: 🌐 HTML5, 📜 JavaScript (ES6+), 🎨 CSS3
* **框架生态**: 💚 Vue.js, ⚛️ React, 🅰️ Angular
* **移动开发**: 📱 微信小程序, 🔧 Vant Weapp, 🔄 uni-app
* **构建工具**: 📦 Webpack, 🛠️ Vite, 🎯 Rollup

#### ⛓️ 区块链技术
* **智能合约**: 🔗 Solidity, 📜 Hardhat, 🧪 Truffle
* **区块链平台**: ⛓️ Ethereum, 🏢 FISCO BCOS
* **Web3 开发**: 🔌 Ethers.js, 🌐 Web3.js

#### 🤖 AI & AR 技术
* **人工智能**: 🤖 AI 客服, 🧠 机器学习
* **增强现实**: 👁️ AR 导览, 🎯 AR 技术
* **计算机视觉**: 📷 OpenCV, 🖼️ 图像处理
* **新兴技术**: 🔮 前沿技术融合

#### ☁️ 云服务与部署
* **云平台**: ☁️ AWS, 🚀 Vercel, 🐳 Docker, ☁️ 阿里云
* **数据库服务**: 🟢 Neon (PostgreSQL), 🍃 MongoDB Atlas, 🐬 MySQL
* **存储服务**: 📁 Vercel Blob, 🪣 AWS S3, 🎥 阿里云视频点播

---

### 🎨 设计、光影与旋律

除了代码，我的生活还有这些色彩：

* **设计 🖌️**: 喜欢琢磨用户界面 (UI) 和用户体验 (UX)，追求简洁与美感的平衡。相信好的设计能让技术更有温度。
* **摄影 📸**: 用镜头捕捉生活中的美好瞬间，无论是壮丽风光还是日常小确幸。摄影教会了我如何用不同的角度看待世界。
* **音乐 🎵**: 音乐是我的灵感源泉，从古典到流行，各种风格都有涉猎。在编码时，音乐总能帮我找到最佳的节奏。
* **写作 ✍️**: 通过文字整理思绪，分享见闻，也希望通过写作与更多人交流。技术写作让我更深入地理解所学知识。

---

### 🌟 我的项目

这里是我最近在折腾的一些有趣项目 🚀：

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 15px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin: 0 0 15px 0; color: white;">📝 个人博客系统</h4>
<p style="margin: 0; font-size: 14px; opacity: 0.9;">🚀 基于 Node.js + Neon + Vercel 的全栈博客，支持动态内容管理和 🎭 Live2D 看板娘，让技术分享更有趣！</p>
<div style="margin-top: 15px; padding: 5px 10px; background: rgba(255,255,255,0.2); border-radius: 10px; display: inline-block; font-size: 12px;">✅ 已完成</div>
</div>

<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 20px; border-radius: 15px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin: 0 0 15px 0; color: white;">🔗 区块链数字证书系统</h4>
<p style="margin: 0; font-size: 14px; opacity: 0.9;">⛓️ 基于以太坊的模块化数字证书 DApp，采用 ERC-721 标准实现证书全生命周期管理。</p>
<div style="margin-top: 15px; padding: 5px 10px; background: rgba(255,255,255,0.2); border-radius: 10px; display: inline-block; font-size: 12px;">✅ 已完成</div>
</div>

<div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 20px; border-radius: 15px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin: 0 0 15px 0; color: white;">🌿 供应链溯源平台</h4>
<p style="margin: 0; font-size: 14px; opacity: 0.9;">🏢 基于 FISCO BCOS 的企业级溯源平台，实现中药材从种植到物流的全流程透明化管理。</p>
<div style="margin-top: 15px; padding: 5px 10px; background: rgba(255,255,255,0.2); border-radius: 10px; display: inline-block; font-size: 12px;">✅ 已完成</div>
</div>

<div style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); padding: 20px; border-radius: 15px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin: 0 0 15px 0; color: white;">🏮 文旅助农小程序</h4>
<p style="margin: 0; font-size: 14px; opacity: 0.9;">🚀 融合区块链、AR、AI等前沿技术的微信小程序，实现农产品溯源、AR导览、AI客服等创新功能。</p>
<div style="margin-top: 15px; padding: 5px 10px; background: rgba(255,255,255,0.2); border-radius: 10px; display: inline-block; font-size: 12px;">✅ 已完成</div>
</div>

<div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 20px; border-radius: 15px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin: 0 0 15px 0; color: white;">🖥️ 屏幕共享系统</h4>
<p style="margin: 0; font-size: 14px; opacity: 0.9;">🎬 基于 Python + Flask + Socket.IO 的多客户端屏幕共享解决方案，实现高性能实时图像传输。</p>
<div style="margin-top: 15px; padding: 5px 10px; background: rgba(255,255,255,0.2); border-radius: 10px; display: inline-block; font-size: 12px;">✅ 已完成</div>
</div>

<div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 20px; border-radius: 15px; color: #333; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h4 style="margin: 0 0 15px 0; color: #333;">🎓 在线教育平台</h4>
<p style="margin: 0; font-size: 14px; opacity: 0.8;">📚 基于 Node.js + Vue.js + uni-app 的全栈教育平台，实现PC网站和移动App多端统一。</p>
<div style="margin-top: 15px; padding: 5px 10px; background: rgba(0,0,0,0.1); border-radius: 10px; display: inline-block; font-size: 12px;">✅ 已完成</div>
</div>

</div>

<div style="text-align: center; margin: 30px 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
<h3 style="margin: 0 0 10px 0; color: white;">🚧 更多精彩项目正在开发中...</h3>
<p style="margin: 0; opacity: 0.9;">敬请期待！✨</p>
</div>

---

### 📬 找到我 & 联系我

你也可以在这些地方找到我，或者通过邮件与我联系 📞：

* **GitHub**: [https://github.com/shimu-ui](https://github.com/shimu-ui) 🐙 (代码与开源项目)
* **Bilibili**: [https://space.bilibili.com/3494375472499132](https://space.bilibili.com/3494375472499132) 📺 (或许会有视频内容？)
* **Email**: [shimuui280@gmail.com](mailto:shimuui280@gmail.com) 📧

---

### 🎯 未来规划

* 深入学习 🦀 Rust 和系统编程
* 探索 AI/ML 领域，特别是大语言模型的应用 🤖
* 尝试更多有趣的技术栈和框架 🚀

---

再次感谢你的来访，希望你在这里能有所收获！🚀 

*"代码改变世界，技术连接未来"* ✨ 
