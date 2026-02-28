"use client";

import { CTAButton } from "@/app/_components/inputs/buttons/CTAButton";
import { useState } from "react";

export const SearchBar = () => {
  const [value, setValue] = useState("");

  return (
    <div className="max-w-[750px] flex rounded-md bg-[#000]">
      <input
        value={value}
        onChange={(e) => setValue(e.target.value)}
        placeholder="Search for title, author, genre"
        className="py-2 px-4 w-full outline-none border-0 text-[#FFF]"
      />

      <div className="p-2">
        <CTAButton
          text="Search"
          textColor="#FFF"
          bgColor="#692592"
          action={() => console.log("Searching")}
        />
      </div>
    </div>
  );
};
