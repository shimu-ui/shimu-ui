<!-- 巨型固定动态表情 -->
<div align="center">
  <svg width="480" height="200" viewBox="0 0 480 200" xmlns="http://www.w3.org/2000/svg">
    <style>
      /* 让表情上下浮动 + 颜色呼吸 */
      @keyframes float {
        0%   { transform: translateY(0px);  }
        50%  { transform: translateY(-20px); }
        100% { transform: translateY(0px);  }
      }
      @keyframes glow {
        0%   { fill: #ff5e62; }
        50%  { fill: #00f5ff; }
        100% { fill: #ff5e62; }
      }
      .emoji {
        font-size: 140px;
        animation: float 2.5s ease-in-out infinite,
                   glow   3s   linear      infinite;
      }
    </style>

    <!-- 背景渐变圆角卡片 -->
    <defs>
      <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0f0c29"/>
        <stop offset="50%" stop-color="#302b63"/>
        <stop offset="100%" stop-color="#24243e"/>
      </linearGradient>
    </defs>
    <rect width="100%" height="100%" rx="30" fill="url(#bg)"/>

    <!-- 巨表情 -->
    <text x="50%" y="52%" dominant-baseline="middle" text-anchor="middle" class="emoji">
      🤖
    </text>

    <!-- 打字机副标题 -->
    <text x="50%" y="88%" font-size="20" font-family="Fira Code" fill="#ffffff" text-anchor="middle">
      <animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite"/>
      Ctrl + S 是信仰
    </text>
  </svg>
</div>
