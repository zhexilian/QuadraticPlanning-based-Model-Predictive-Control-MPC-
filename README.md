# QuadraticPlanning-based-Model-Predictive-Control-MPC-with-cruising-and-lane-change-capability
A intelligent vehicle Model Predictive Control(MPC) implementation using QuadraticPlanning. The controller is coded in Python. **That's because it is more suitable for using Python in traffic simulation (vissim, sumo) or RL training.**  
**more details can be found in documentation.**  
Following video describes a full process of lane-changing and adapt cruising.  
<video src='https://github.com/zhexilian/QuadraticPlanning-based-Model-Predictive-Control-MPC-/assets/148358711/3dbdeba2-2151-485a-a6ea-15d7aa25f9ba' width=100/>   
  
**# CASE 1. adaptive cruise control**  
Ego vehicle with the proposed controller aims to adaptive cruise to the preceding vehicle. Here are speed and postion figures of the two vehicles. It demonstrates that the ego vehicle speeds up to pursue the desired following distance and finally deccelarates to follow the target speed (which is the speed of the preceding vehicle).  

![图片](https://github.com/zhexilian/QuadraticPlanning-based-Model-Predictive-Control-MPC-/assets/148358711/dc21112f-8b0d-480a-82b1-2612bbeed037) ![图片](https://github.com/zhexilian/QuadraticPlanning-based-Model-Predictive-Control-MPC-/assets/148358711/28d0a5a0-cff9-44d5-b5bc-2f68f08a8aa2)

**# CASE 2. lane-change**  
Ego vehicle with the proposed controller aims to change lane, as shown in the following figure. It can be seen that the lane-change process is fast. The figure in right shown the lane-change process from a BEV view.    
![图片](https://github.com/zhexilian/QuadraticPlanning-based-Model-Predictive-Control-MPC-/assets/148358711/cfaa969f-2037-434c-a3ca-6655f01d3750) ![图片](https://github.com/zhexilian/QuadraticPlanning-based-Model-Predictive-Control-MPC-/assets/148358711/fa46af7b-1200-43cf-b227-de65f59d4ebe)




