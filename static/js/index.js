let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [1, 2, 3, 4, 5, 6,7,8] },
        { orderable: false, targets: [5, 6] },
        { searchable: false, targets: [5, 6] }
    ],
    pageLength: 4,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listCotizaciones();

    dataTable = $("#datatable-vcp").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listCotizaciones = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/cuotapartes/list_cotizaciones');
        const data = await response.json();
        
        let content = ``;
        data.cotizaciones_vcps.forEach((cotizaciones_vcp, index) => {
            content += `
                <tr>
                    <td>${index}</td>
                    <td>${cotizaciones_vcp.fondo_id_id}</td>
                    <td>${cotizaciones_vcp.fecha_cotizacion}</td>
                    <td>${cotizaciones_vcp.cuota}</td>
                    <td>${cotizaciones_vcp.patrimonio}</td>
                    <td>${cotizaciones_vcp.market_share}</td>
                    <td>${cotizaciones_vcp.cantidad_de_cuotas}</td>
                    <td>${cotizaciones_vcp.moneda}</td>
                </tr>`;
        });
        tableBody_cotizaciones_vcp.innerHTML = content;
        
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});