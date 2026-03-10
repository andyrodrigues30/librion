"use client";

import { BookCover } from "../BookCover";

export const RecentlyAddedList = () => {
  const covers = Array.from({ length: 6 });

  return (
    <div className="w-screen lg:flex lg:justify-center lg:items-center text-[#FFF] p-12">
      <div className="p-8">
        <h2 className="uppercase text-[4rem]">Recently<br/>Added</h2>
        <p className="py-6">A spotlight of books recently added to the collection.</p>
      </div>

      <div className="flex max-w-[1250px] overflow-x-auto m-4">
        {covers.map((_, index) => {
          return <BookCover key={index} width={230} height={320} />;
        })}
      </div>
    </div>
  );
};