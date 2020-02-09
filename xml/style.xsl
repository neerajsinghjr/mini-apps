<!--=============================================
XSLT|eXtensible Stylesheet Language Transformation 
=================================================-->
<?xml version="1.0"?>

<!-- xsl  -->
<xsl:stylesheet version="1.0"
	xmlns:xsl = "http://www.w3.org/1999/XSL/Tranform">

<xsl:template match="/">

<html>
<head>
<style>
temp > temp-1 {
	font-size: 20px;
	font-weight: bolder;
	width: 80px;
	height: 30px;
	line-height: 40px;
}

temp > temp-2 {
	font-size: 30px;
	font-weight: bolder;
	width: 80px;
	height: 30px;
	line-height: 40px;
}

temp > temp-3 {
	font-size: 40px;
	font-weight: bolder;
	width: 80px;
	height: 30px;
	line-height: 40px;
}
</style>
</head>
<body>
	<xsl:apply-templates/>
</body>
</html>
</xsl:template>

<xsl:template match="temp">
	<span class="temp-1">
		<xsl:value-of