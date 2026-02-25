import type { Metadata } from "next";
import "./globals.css";


export const metadata: Metadata = {
  title: "Librion",
  description: "An open-source, self-hosted library management system designed for small to medium libraries.",
};


export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
