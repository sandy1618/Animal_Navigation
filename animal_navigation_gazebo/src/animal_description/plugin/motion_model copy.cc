#include <functional>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <ignition/math/Vector3.hh>

namespace gazebo {
    class Motion_Model : public ModelPlugin 
    {
        private : 
        // Pointer to the model
            physics::ModelPtr model;
        // Pointer to the update event connection 
            event::ConnectionPtr updateConnection;
        public: 
            void Load(physics::ModelPtr _parent, sdf::ElementPtr _sdf)
            {
                // Store the pointer to model 
                this -> model = _parent;

                // Listen to the update event . This event is broadcasted every simulation iteration
                this-> updateConnection = event::Events::ConnectWorldUpdateBegin(
                    std::bind(&Motion_Model::OnUpdate,this) // bind returns this.OnUpdate() to ConnectWorldUpdateBegin
                );
                
            }
            // Called by the world update start event 
            public:
                void OnUpdate(){
                    // Apply a small linear velocity to the modle 
                    this->model->SetLinearVel(ignition::math::Vector3d(0.3,0,0));
                }
            
    };
    // Register the plugin with the simulator
    GZ_REGISTER_MODEL_PLUGIN(Motion_Model)
}