import React from "react";
import AdventureStatCard from "../components/AdenturerCard";

const Page = () => {
  return (
    <div className="min-h-dvh bg-red-500 py-10 flex items-center justify-center">
      <div className="grid grid-cols-2 gap-6 w-full max-w-[1440px]">
        <AdventureStatCard />
        <AdventureStatCard />
        <AdventureStatCard />
      </div>
    </div>
  );
};

export default Page;