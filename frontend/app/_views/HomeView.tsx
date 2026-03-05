"use client";

import { RecentlyAddedList } from "@/app/_components/grids/RecentlyAddedList";
import { Searchbar } from "../_components/inputs/field/Searchbar";
import { GenreGrid } from "../_components/grids/GenreGrid";

export const Homeview = () => {
  return (
    <div>
      <RecentlyAddedList />

      <div className="flex justify-center items-center">
        <Searchbar
          placeholder="Enter title, author, genre"
          action={() => console.log("Searching...")}
        />
      </div>

      <div className="flex justify-center items-center">
      <GenreGrid />
    </div>
    </div>
  );
};
