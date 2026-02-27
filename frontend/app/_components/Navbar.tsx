"use client";

import { JSX, useState } from "react";
import Image from "next/image";
import Logo from "../../public/logo.svg";

type NavLink = {
  name: string;
  href: string;
};

const navLinks: NavLink[] = [
  { name: "Browse", href: "/browse" },
  { name: "New", href: "/new" },
  { name: "Profile", href: "/profile" },
  { name: "Manage", href: "/manage" },
  { name: "Dashboard", href: "/dashboard" },
];

interface ButtonProps {
  text: string;
  bgColor: string;
  textColor: string;
}

export const CTAButton = ({ text, bgColor, textColor }: ButtonProps) => {
  return (
    <button
      className={`w-full mt-2 px-5 py-2 rounded-md bg-[${bgColor}] text-[${textColor}]`}
    >
      {text}
    </button>
  );
};

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
              <a
                key={link.name}
                href={link.href}
                className="text-white"
              >
                {link.name}
              </a>
            ))}
          </div>

          <div className="hidden md:block px-4">
            <CTAButton text="Borrow" bgColor="#00AB97" textColor="#000" />
          </div>

          {/* Mobile Menu Button */}
          <div className="md:hidden">
            <button
              onClick={() => setIsOpen((prev) => !prev)}
              className="text-gray-700 focus:outline-none px-4"
              aria-label="Toggle menu"
            >
              <svg
                className="w-6 h-6"
                fill="none"
                stroke="#FFF"
                viewBox="0 0 24 24"
              >
                {isOpen ? (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M6 18L18 6M6 6l12 12"
                  />
                ) : (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                )}
              </svg>
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Dropdown */}
      {isOpen && (
        <div className="md:hidden border-t bg-black">
          <div className="px-6 py-4 space-y-4">
            {navLinks.map((link) => (
              <a
                key={link.name}
                href={link.href}
                className="block text-white font-medium hover:text-blue-600 transition"
              >
                {link.name}
              </a>
            ))}

            <CTAButton text="Borrow" bgColor="#00AB97" textColor="#000" />
          </div>
        </div>
      )}
    </nav>
  );
}
