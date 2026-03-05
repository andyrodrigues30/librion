"use client";

import { useState } from "react";

import { SearchbarProps } from "@/app/_types/Searchbar";
import { CTAButton } from "@/app/_components/inputs/buttons/CTAButton";

export const Searchbar = ({ placeholder, action }: SearchbarProps) => {
  const [value, setValue] = useState("");

  return (
    <div className="max-w-[750px] w-full flex rounded-md bg-[#000]">
      <input
        value={value}
        onChange={(e) => setValue(e.target.value)}
        placeholder={placeholder}
        className="py-2 px-4 w-full outline-none border-0 text-[#FFF]"
      />

      <div className="p-2">
        <CTAButton
          text="Search"
          textColor="#FFF"
          bgColor="#692592"
          action={action}
        />
      </div>
    </div>
  );
};
