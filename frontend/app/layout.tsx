import type { Metadata } from "next";
import Navbar from "@/app/_components/navigation/Navbar";
import "@/app/globals.css";

export const metadata: Metadata = {
  title: "Librion",
  description:
    "An open-source, self-hosted library management system designed for small to medium libraries.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <Navbar />

        {children}
      </body>
    </html>
  );
}
