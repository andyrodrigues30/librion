import type { MetadataRoute } from "next"
 
export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Librion - Library Management",
    short_name: "Librion",
    description: "An open-source, self-hosted library management system designed for small to medium libraries.",
    start_url: "/",
    display: "standalone",
    background_color: "#000000",
    theme_color: "#00AB97",
    icons: [
      {
        src: "/favicon.ico",
        sizes: "any",
        type: "image/x-icon",
      },
      {
        src: "/assets/icon.svg",
        sizes: "480x480",
        type: "image/x-icon",
      },
      {
        src: "/assets/apple-icon.png",
        sizes: "180x180",
        type: "image/x-icon",
      },
      {
        src: "/assets/icon-192.png",
        sizes: "192x192",
        type: "image/x-icon",
      },
      {
        src: "/assets/icon-512.png",
        sizes: "512x512",
        type: "image/x-icon",
      },
    ],
  }
}