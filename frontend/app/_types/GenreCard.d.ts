export interface Genre {
  type: string;
  path: string;
}

export interface GenreCardProps {
  key: number;
  genre: Genre;
}