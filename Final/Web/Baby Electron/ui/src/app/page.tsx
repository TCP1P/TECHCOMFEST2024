"use client"
import { useRouter } from "next/navigation";

export default function Home() {
  const history = useRouter();

  const handleButtonClick = () => {
    history.push('/form');
  };

  return (
    <main className="flex flex-col w-full border-opacity-50 min-h-screen">
      <div className="grid place-items-center min-h-screen">
        <div className="hero min-h-screen bg-base-200">
          <div className="hero-content text-center">
            <div className="max-w-md">
              <h1 className="text-5xl font-bold">Hello There!</h1>
              <p className="py-6">This is the website for you to send your payload</p>
              <button className="btn btn-primary" onClick={handleButtonClick}>
                Get Started
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
