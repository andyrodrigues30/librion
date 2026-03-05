import type { Metadata } from "next";
import Navbar from "@/app/_components/navigation/Navbar";
import "@/app/globals.css";
import { BubblesBg } from "@/app/_components/BubblesBg";

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
      <body className="bg-[#000]">
        <BubblesBg />

        <div className="top-0 left-0 p-4 w-screen h-screen overflow-x-hidden overflow-y-auto absolute z-5">
          <Navbar />
          {children}
        </div>
      </body>
    </html>
  );
}
