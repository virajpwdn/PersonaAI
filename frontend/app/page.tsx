import gsap from "gsap";
import {ScrollTrigger} from 'gsap/ScrollTrigger'
import Hero from "./components/Hero";

gsap.registerPlugin(ScrollTrigger)
const page = () => {
  return <div>
    <Hero />
  </div>;
};
export default page;
