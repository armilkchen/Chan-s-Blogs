export const config = {
  site: {
    title: "Chan's Blogs",
    name: "Chan's Blogs",
    description: "An investment in knowledge pays the best interest.",
    keywords: ["SEO", "AI", "Full Stack Developer"],
    url: "https://chanblog.xyz",
    baseUrl: "https://chanblog.xyz",
    image: "https://chanblog.xyz/og-image.png",
    favicon: {
      ico: "/favicon.ico",
      png: "/favicon.png",
      svg: "/favicon.svg",
      appleTouchIcon: "/favicon.png",
    },
    manifest: "/site.webmanifest",
    rss: {
      title: "Chan's Blogs",
      description: "Chan's Blogs - Share my learning and experience",
      feedLinks: {
        rss2: "/rss.xml",
        json: "/feed.json",
        atom: "/atom.xml",
      },
    },
  },
  author: {
    name: "chan",
    email: "changroup1902@gmail.com",
    bio: "An investment in knowledge pays the best interest.",
  },
  social: {
    github: "https://github.com/xxx",
    x: "https://x.com/xxx",
    xiaohongshu: "https://www.xiaohongshu.com/user/profile/xxx",
    wechat: "https://storage.xxx.com/images/wechat-official-account.png",
    buyMeACoffee: "https://www.buymeacoffee.com/xxx",
  },
  giscus: {
    repo: "armilkchen/Chan-s-Blogs",
    repoId: "R_kgDOOXyo2A",
    categoryId: "DIC_kwDOOXyo2M4Co_uZ",
  },
  navigation: {
    main: [
      { 
        title: "文章", 
        href: "/blog",
      },
    ],
  },
  seo: {
    metadataBase: new URL("https://chanblog.xyz"),
    alternates: {
      canonical: './',
    },
    openGraph: {
      type: "website" as const,
      locale: "zh_CN",
    },
    twitter: {
      card: "summary_large_image" as const,
      creator: "@xxx",
    },
  },
};
