//------------------------------------------------------------------------------
//--------------------------Universidade de Sao Paulo---------------------------
//----------------------Escola de Engenharia de Sao Carlos----------------------
//----------------Departamento de Engenharia de Estruturas - SET----------------
//------------------------------Sao Carlos - 2018-------------------------------
//------------------------------------------------------------------------------
  
//------------------------------------------------------------------------------
//---------------------------------Developed by---------------------------------
//--------------------------------Patricia Tonon--------------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//--------------------GENERATION OF CAVITY ISOGEOMETRIC MESH--------------------
//------------------------------------------------------------------------------
// C++ standard libraries
#include <fstream>
#include <iostream>

// Boost libraries

#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/vector.hpp>

using namespace boost::numeric;
using namespace std;

int main () 
{
	string line;
   
	// Starting the data reading
    std::ifstream data;

    data.open("points.dat");

    int numberPoints;

    data >> numberPoints;

    double coord[numberPoints][3];
    getline(data,line);

    for (int i = 0; i < numberPoints; i++){

    	data >> coord[i][0] >> coord[i][1] >> coord[i][2];
    	getline(data,line);

    }

    int numberCell;
    data >> numberCell;
    getline(data,line);

    int con[numberCell][27];

    for (int i = 0; i < numberCell; i++){

    	data >> con[i][0] >> con[i][1] >> con[i][2] >> con[i][3] >> con[i][4] >> con[i][5] >> con[i][6] >> con[i][7] >> 
    	con[i][8] >> con[i][9] >> con[i][10] >> con[i][11] >> con[i][12] >> con[i][13] >> con[i][14] >> con[i][15] >> con[i][16] >> 
    	con[i][17] >> con[i][18] >> con[i][19] >> con[i][20] >> con[i][21] >> con[i][22] >> con[i][23] >> con[i][24] >> con[i][25] >> 
    	con[i][26];

    	getline(data,line);
    }


	std::ofstream mesh;
	mesh.open("mesh.msh", std::ofstream::out | std::ofstream::app);

	mesh << "$MeshFormat" << std::endl;
	mesh << "2.2 0 8" << std::endl;
	mesh << "$EndMeshFormat" << std::endl;
	mesh << "$PhysicalNames" << std::endl;
	mesh << "1" << std::endl;
	mesh << "1 1 Volume" << std::endl;
	mesh << "$EndPhysicalNames" << std::endl;
	mesh << "$Nodes" << std::endl;
	mesh << numberPoints << std::endl;

	for (int i = 0; i < numberPoints; i++){

		mesh << i+1 << " " << coord[i][0] << " " << coord[i][1] << " " << coord[i][2] << std::endl;

	}

	mesh << "$EndNodes" << std::endl;

	mesh << "$Elements" << std::endl;

		mesh << numberCell << std::endl;

		for (int i = 0; i < numberCell; i++){

			mesh << i+1 << " 12 2 1 1 " <<  con[i][0]+1 << " " <<  con[i][1]+1 << " " << con[i][2]+1 << " " << con[i][3]+1 << " " << con[i][4]+1 << " " << con[i][5]+1 << " " << con[i][6]+1 << " " << con[i][7]+1 << " " <<
    		con[i][8]+1 << " " << con[i][9]+1 << " " << con[i][10]+1 << " " << con[i][11]+1 << " " << con[i][12]+1 << " " << con[i][13]+1 << " " << con[i][14]+1 << " " << con[i][15]+1 << " " << con[i][16]+1 << " " <<
    		con[i][17]+1 << " " << con[i][18]+1 << " " << con[i][19]+1 << " " << con[i][20]+1 << " " << con[i][21]+1 << " " << con[i][22]+1 << " " << con[i][23]+1 << " " << con[i][24]+1 << " " << con[i][25]+1 << " " << 
    		con[i][26]+1 << std::endl;

		}

	mesh << "$EndElements" << std::endl;


   
return 0;

};


 
  




 
