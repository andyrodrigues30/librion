"use client";

export const RecentlyAddedList = () => {
  const covers = Array.from({ length: 6 });

  return (
    <div className="lg:flex lg:justify-start lg:items-center text-[#FFF] p-12">
      <div className="p-8">
        <h2 className="uppercase text-[4rem]">Recently Added</h2>
        <p>A spotlight of books recently added to the collection.</p>
      </div>

      <div className="flex overflow-x-auto m-4 rounded-md">
        {covers.map((_, index) => {
          return <BookCover key={index} />;
        })}
      </div>
    </div>
  );
};

const BookCover = () => {
  return (
    <div className="w-[230px] h-[320px] m-2 bg-[#202020] rounded-lg flex-shrink-0" />
  );
};
