
#pragma once
#include <cmath>

// Force isnan into the global scope if the compiler expects it there
using std::isnan;
using std::isinf; // Safety bonus for other potential strict compiler drops
