import type { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
  return [
  {
    "url": "/",
    lastModified: new Date("2025-04-14T09:13:35.824Z"),
    "changeFrequency": "daily",
    "priority": 1
  },
  {
    "url": "/blog",
    lastModified: new Date("2025-04-14T09:13:35.825Z"),
    "changeFrequency": "daily",
    "priority": 0.9
  },
  {
    "url": "blog/20250414-1",
    lastModified: new Date("2025-04-14T12:10:00.000Z"),
    "changeFrequency": "weekly",
    "priority": 0.8
  }
]
}
