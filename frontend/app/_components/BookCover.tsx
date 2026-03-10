"use client";

import { BookCoverProps } from "../_types/BookCard";

export const BookCover = ({width, height}: BookCoverProps) => {
  return (
    // TODO: make cover clickable
    <div
        style={{ width: `${width}px`, height: `${height}px` }}
        className=" m-2 bg-[#202020] rounded-lg flex-shrink-0"
    />
  );
};