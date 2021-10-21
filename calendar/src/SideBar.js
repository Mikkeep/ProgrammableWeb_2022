import {BsPlus, BsGearFill} from 'react-icons/bs';
import { FaUserCircle } from 'react-icons/fa';

const Sidebar = () => {
    return (
        <div className="fixed top-0 left-0 h-screen w-16 m-0
                        flex flex-col
                        bg-blue-300 dark:bg-red-800 text-gray-600 shadow-md">
            <SideBarIcon icon={<FaUserCircle size="30" />} text={"Your profile"} />
            <SideBarIcon icon={<BsPlus size="30" />} text={"Add new event"} />
            <SideBarIcon icon={<BsGearFill size="20" />} text={"Settings"} />
        </div>
    );
};

const SideBarIcon = ({ icon, text }) => (
    <div className="sidebar-icon group">
        {icon}
    <span class="sidebar-setting group-hover:scale-125">
        {text}
    </span>
    </div>
);

export default Sidebar;