
__all__ = ["dataframe_h"]



dataframe_h ="\
    namespace xAOD{\
        struct cell_t{\
          float e;\
          float et;\
          float eta;\
          float phi;\
          float deta;\
          float dphi;\
        };\
        struct CaloCell_t{\
          float e;\
          float et;\
          float eta;\
          float phi;\
          float deta;\
          float dphi;\
          int descriptor_link;\
        };\
        struct CaloDetDescriptor_t{\
          int sampling;\
          int detector;\
          float eta;\
          float phi;\
          float deta;\
          float dphi;\
          float rmin;\
          float rmax;\
          float e;\
          float etruth;\
          int bcid_start;\
          int bcid_end;\
          int bcid_truth;\
          float bc_duration;\
          unsigned int hash;\
          int cell_link;\
        };\
        struct CaloCluster_t{\
          float e;\
          float et;\
          float eta;\
          float phi;\
          float deta;\
          float dphi;\
          float e0;\
          float e1;\
          float e2;\
          float e3;\
          float ehad1;\
          float ehad2;\
          float ehad3;\
          float etot;\
          float e233;\
          float e237;\
          float e277;\
          float emaxs1;\
          float emaxs2;\
          float e2tsts1;\
          float reta;\
          float rphi;\
          float rhad;\
          float rhad1;\
          float eratio;\
          float f0;\
          float f1;\
          float f2;\
          float f3;\
          float weta2;\
          std::vector<float> rp_values;\
          std::vector<int> cell_links;\
        };\
        struct CaloRings_t{\
          int cluster_link;\
          std::vector<float> rings;\
        };\
        struct EventInfo_t{\
          float eventNumber;\
          float avgmu;\
        };\
        struct TruthParticle_t{\
          int pdgid;\
          float e;\
          float et;\
          float eta;\
          float phi;\
          float px;\
          float py;\
          float pz;\
        };\
      }"
