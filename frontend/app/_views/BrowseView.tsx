"use client";

import { BookGrid } from "@/app/_components/grids/BookGrid";
import { Searchbar } from "../_components/inputs/field/Searchbar";

export const BrowseView = () => {
    return (
        <div className="flex flex-col justify-start items-center max-w-[1275px]">
            <Searchbar
                placeholder={"Search for title, author, genre"}
                action={() => console.log("Searching...") }
            />

            <BookGrid />
        </div>
    )
}