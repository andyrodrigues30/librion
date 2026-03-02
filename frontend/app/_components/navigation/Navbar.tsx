"use client";

import { JSX, useState } from "react";
import Image from "next/image";

import {
  MobileDropdown,
  MobileMenuBtn,
} from "@/app/_components/navigation/MobileNavbar";
import { CTAButton } from "@/app/_components/inputs/buttons/CTAButton";
import { NavLink } from "@/app/_types/Navbar";

import Logo from "@/public/logo.svg";

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
    <nav className="flex items-center justify-between h-22 px-4">
      <Image
        src={Logo}
        alt="Logo"
        width={172}
        height={66}
        priority
        className="h-12 w-auto"
      />

      <div className="hidden md:flex">
        {navLinks.map((link) => (
          <a key={link.name} href={link.href} className="text-white p-4">
            {link.name}
          </a>
        ))}
      </div>

      <div className="hidden md:block p-4">
        <CTAButton
          text="Borrow"
          bgColor="#00AB97"
          textColor="#000"
          action={() => console.log("click")}
        />
      </div>

      <MobileMenuBtn isOpen={isOpen} setIsOpen={setIsOpen} />

      {isOpen && <MobileDropdown navLinks={navLinks} />}
    </nav>
  );
}
