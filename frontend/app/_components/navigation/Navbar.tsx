"use client";

import { JSX, useState } from "react";
import Image from "next/image";
import Logo from "@/public/logo.svg";
import { NavLink } from "@/app/_types/Navbar";
import { MobileDropdown, MobileMenuBtn } from "@/app/_components/navigation/MobileNavbar";
import { ButtonProps } from "@/app/_types/Button";

const navLinks: NavLink[] = [
  { name: "Browse", href: "/browse" },
  { name: "New", href: "/new" },
  { name: "Profile", href: "/profile" },
  { name: "Manage", href: "/manage" },
  { name: "Dashboard", href: "/dashboard" },
];

export default function Navbar(): JSX.Element {
  const [isOpen, setIsOpen] = useState<boolean>(false);

  return (
    <nav className="w-full bg-black sticky top-0 z-50">
      <div className="max-w-7xl mx-auto">
        <div className="flex items-center justify-between h-16 relative">
          <Image
            src={Logo}
            alt="Logo"
            width={172}
            height={66}
            priority
            className="h-12 w-auto px-4"
          />

          <div className="hidden md:flex space-x-8 absolute left-1/2 -translate-x-1/2">
            {navLinks.map((link) => (
              <a key={link.name} href={link.href} className="text-white">
                {link.name}
              </a>
            ))}
          </div>

          <div className="hidden md:block px-4">
            <CTAButton text="Borrow" bgColor="#00AB97" textColor="#000" />
          </div>

          <MobileMenuBtn isOpen={isOpen} setIsOpen={setIsOpen} />
        </div>
      </div>

      {isOpen && <MobileDropdown navLinks={navLinks} />}
    </nav>
  );
}

export const CTAButton = ({ text, bgColor, textColor }: ButtonProps) => {
  return (
    <button
      style={{ backgroundColor: bgColor, color: textColor }}
      className="w-full mt-2 px-5 py-2 rounded-md"
    >
      {text}
    </button>
  );
};
