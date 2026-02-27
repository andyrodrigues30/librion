import { NavLink } from "@/app/_types/Navbar";
import { CTAButton } from "@/app/_components/navigation/Navbar";

export const MobileDropdown = ({ navLinks }: { navLinks: NavLink[] }) => {
  return (
    <div className="md:hidden border-t bg-black">
      <div className="px-6 py-4 space-y-4">
        {navLinks.map((link: NavLink) => (
          <a
            key={link.name}
            href={link.href}
            className="block text-white font-medium hover:text-blue-600 transition"
          >
            {link.name}
          </a>
        ))}

        <CTAButton text="Borrow" bgColor="#00AB97" textColor="#000" />
      </div>
    </div>
  );
};

export const MobileMenuBtn = ({
  isOpen,
  setIsOpen,
}: {
  isOpen: boolean;
  setIsOpen: React.Dispatch<React.SetStateAction<boolean>>;
}) => {
  return (
    <div className="md:hidden">
      <button
        onClick={() => setIsOpen((prev: boolean) => !prev)}
        className="text-gray-700 focus:outline-none px-4"
        aria-label="Toggle menu"
      >
        <svg className="w-6 h-6" fill="none" stroke="#FFF" viewBox="0 0 24 24">
          {isOpen ? (
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M6 18L18 6M6 6l12 12"
            />
          ) : (
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M4 6h16M4 12h16M4 18h16"
            />
          )}
        </svg>
      </button>
    </div>
  );
};