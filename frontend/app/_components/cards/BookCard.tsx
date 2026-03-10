"use client";

import { BookCover } from "@/app/_components/BookCover";

export const BookCard = () => {
  return (
    <div className="flex flex-col justify-center items-center">
      <BookCover width={200} height={280} />
      <h3 className="text-[#FFF] text-lg">Book Name</h3>
      <p className="text-[#FFF]">Author Name</p>
    </div>
  );
};
