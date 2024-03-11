# QuadraticPlanning-based-Model-Predictive-Control-MPC-with-cruising-and-lane-change-capability
A intelligent vehicle Model Predictive Control(MPC) implementation using QuadraticPlanning. The controller is coded in Python. **That's because it is more suitable for using the controller in traffic simulation (vissim, sumo) or RL training.**  
**more details can be found in documentation.**  

**# CASE 1. adaptive cruise control**  
Ego vehicle with the proposed controller aims to adaptive cruise to the preceding vehicle. Here are speed and postion figures of the two vehicles. It demonstrates that the ego vehicle speeds up to pursue the desired following distance and finally deccelarates to follow the target speed (which is the speed of the preceding vehicle).  

![图片](https://github.com/zhexilian/QuadraticPlanning-based-Model-Predictive-Control-MPC-/assets/148358711/dc21112f-8b0d-480a-82b1-2612bbeed037) ![图片](https://github.com/zhexilian/QuadraticPlanning-based-Model-Predictive-Control-MPC-/assets/148358711/28d0a5a0-cff9-44d5-b5bc-2f68f08a8aa2)

**# CASE 2. lane-change**  
Ego vehicle with the proposed controller aims to change lane, as shown in the following figure.  
![图片](https://github.com/zhexilian/QuadraticPlanning-based-Model-Predictive-Control-MPC-/assets/148358711/f574467a-4b3c-4d11-8ddb-2f1a2ad40ba0)


