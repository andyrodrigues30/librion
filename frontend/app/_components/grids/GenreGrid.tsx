import { Genre } from "@/app/_types/GenreCard";
import { GenreCard } from "../cards/GenreCard";

export const GenreGrid = () => {
  const genres:  Genre[] = [
    { "type": "Fiction", "path": "/search?genre=fiction" },
    { "type": "Non-fiction", "path": "/search?genre=non-fiction" },
    { "type": "Mystery", "path": "/search?genre=mystery" },
    { "type": "Sci-fi", "path": "/search?genre=sci-fi" },
    { "type": "Romance", "path": "/search?genre=romance" },
    { "type": "Classics", "path": "/search?genre=classics" },
    { "type": "Historical", "path": "/search?genre=historical" },
    { "type": "Mythology", "path": "/search?genre=mythology" },
    { "type": "Y/A", "path": "/search?genre=ya"}
  ];

  return (
    <div className="flex flex-wrap justify-center max-w-[1275px] items-center m-4 md:m-8">
      {genres.map((genre, index) => {
        return <GenreCard key={index} genre={genre} />
      })}
    </div>
  );
}
