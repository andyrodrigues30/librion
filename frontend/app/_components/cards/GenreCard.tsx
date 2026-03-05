import { GenreCardProps } from "@/app/_types/GenreCard";

export const GenreCard = ({ genre }: GenreCardProps) => {
  return (
    <div
      onClick={() => console.log(genre.path)}
      className="w-[250px] p-6 m-4 bg-[#202020] shadow-md rounded-md text-center text-[#FFF]"
    >
      <p>{genre.type}</p>
    </div>
  );
}
