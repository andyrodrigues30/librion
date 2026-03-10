"use client";

import { BookCard } from "../cards/BookCard";

export const BookGrid = () => {
  const books = Array.from({ length: 18 });

  return (
    <div className="p-8 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
      {books.map((book, index) => {
        return <BookCard key={index} />;
      })}
    </div>
  );
};
