import { ButtonProps } from "@/app/_types/Button";

export const CTAButton = ({ text, bgColor, textColor, action }: ButtonProps) => {
  return (
    <button
      style={{ backgroundColor: bgColor, color: textColor }}
      className="w-full px-8 py-2 rounded-md"
      onClick={action}
    >
      {text}
    </button>
  );
};
