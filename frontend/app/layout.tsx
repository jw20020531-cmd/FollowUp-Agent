import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "FollowUp AI",
  description: "An evidence-first follow-up tracking prototype."
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}

