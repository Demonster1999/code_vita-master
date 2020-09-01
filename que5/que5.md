Problem Description
Given blocks of IPV4 CIDR addresses mapped to region name. Find which region does a given IP belongs to.

For better information about how CIDR works. Please refer to the following link.      
https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing

The above link describes IPV6 CIDR also. However, in this problem we are dealing only with IPV4 CIDR only.

CIDR denotes a range of IP addresses. In our problem a region will be assigned a range of CIDRs. All such IP addresses falling in all such CIDR ranges, thus belongs to this given region. Consider an example below.

Example:

Range: 255.1.255.0/23 255.1.255.0/24 India

The CIDR 255.1.255.0/23 can have 512 hosts, and CIDR 255.1.255.0/24 can have 256 hosts. These are the individual ranges denoted by the first and the second CIDRs respectively. Similarly, in between these two ranges of CIDRs there will be other CIDR ranges like

255.1.255.1/23, 255.1.255.2/23 ................ 255.1.254.253/24, 255.1.254.254/24, 255.1.255.0/24

If the number of hosts in each such CIDR range mentioned above is calculated, then the total number of hosts in this overall range exceeds one billion. Now, your task is to find if the given IP address falls in this range.

Consider IP addresses:    255.1.254.123 and 255.1.250.23

Upon performing CIDR expansion, we realize that address 255.1.254.123 falls in this range and hence belongs to India region. However, address 255.1.250.23 does not fall in this region and hence does not belong to India region.

Give R IPv4 CIDR ranges, each belonging to a given region and N IP addresses, your task is to find out the region that a given IP address belongs to.

Constraints
1 < = R <= 100
1 <= N <= 5*10 ^ 4

Input
First line contains 2 space separated integers R and N, where R denotes number of IPv4 CIDR ranges and N denotes number of IP addresses
Next R lines contains two CIDR ranges (from range and to range) and region name. All three inputs are space separated
Next N lines, each contain a single IPV4 address

Output
For each IPV4 address, print the respective region name it belongs to. If it belongs to no region, then print “None” as output.

Time Limit
2

Examples
Example 1

Input

1 3
201.100.255.0/20 207.105.25.0/24 Bangladesh
202.251.245.56
202.255.245.230
207.106.245.230

Output

Bangladesh
Bangladesh
None

Explanation

Given R = 1, N = 3

The CIDR 201.100.255.0/20 can have 4096 hosts, and CIDR 207.105.25.0/24 can have 256 hosts. These are the individual ranges denoted by the first and the second CIDRs respectively. Similarly, in between these two ranges of CIDRs there will other CIDR ranges like

201.100.255.1/20, 201.100.255.2/20 ................ 207.105.24.253/24, 207.105.24.254/24, 207.105.25.0/24

Address 202.251.245.56 and 202.255.245.230 belong to this region. However, 207.106.245.230 does not belongs to this region.

So, output will be:
Bangladesh
Bangladesh
None

Example 2

Input

2 5
7.25.255.0/20 12.175.25.0/24 Taiwan
13.25.255.0/20 19.175.25.0/24 Japan
14.30.2.0
20.30.2.0
13.25.240.0
8.30.2.0
19.175.25.255

Output

Japan
None
Japan
Taiwan
Japan

Explanation

Given R = 2, N = 4

The CIDR 7.25.255.0/20 can have 4096 hosts, and 12.175.25.0/24 can have 256 hosts. These are the individual ranges denoted by the first and the second CIDRs respectively for Taiwan region. Similarly, in between these two ranges of CIDRs there will other CIDR ranges like

7.25.255.1/20, 7.25.255.2/20 ................ 12.175.24.254/24, 12.175.24.255/24, 12.175.25.0/24

Similarly for Japan region,

The CIDR 13.25.255.0/20 can have 4096 hosts, and 19.175.25.0/24 can have 256 hosts. These are the individual ranges denoted by the first and the second CIDRs respectively for Japan region. Similarly, in between these two ranges of CIDRs there will other CIDR ranges like

13.25.255.1/20, 13.25.255.2/20 ................ 19.175.24.254/24, 19.175.24.255/24, 19.175.25.0

Upon computation, we realize that addresses 14.30.2.0, 13.25.240.0 and 19.175.25.255 belong to Japan region and address 8.30.2.0 belongs to Taiwan region, while address 20.30.2.0 belongs to neither of the two regions.

Hence the output is,

Japan
None
Japan
Taiwan
Japan